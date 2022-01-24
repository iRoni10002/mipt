from abc import ABC, abstractmethod
from random import randint


class Chain(ABC):
    right_base = ['A', 'T', 'G', 'C']
    @abstractmethod
    def __init__(self, chain):
        for base in chain:
            if base not in self.right_base:
                raise ValueError
        self.chain = chain

    @abstractmethod
    def get_one_base(self, i):
        pass

    def get_complement_DNK(self):
        complement_chain = ''
        for base in self.chain:
            complement_chain += self.equal_bases[base]
        return(complement_chain)

    def __add__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return self.chain + other.chain
        else:
            raise TypeError

    def __mul__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            first_chain = self.chain
            second_chain = other.chain
            if len(second_chain) > len(first_chain):
                first_chain, second_chain = second_chain, first_chain
            result_chain = ''
            for i in range(len(second_chain)):
                result_chain += [first_chain[i], second_chain[i]][randint(0, 1)]
            result_chain += first_chain[len(second_chain)::]
            return result_chain
        else:
            raise TypeError

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class RNK(Chain):
    right_base = ['A', 'U', 'G', 'C']
    def __init__(self, chain):
        super().__init__(chain)
        self.equal_bases = {
                            'A': 'T',
                            'U': 'A',
                            'G': 'C',
                            'C': 'G'
                            }

    def get_one_base(self, i):
        return self.chain[i]

    def __repr__(self):
        return 'RNK: {}'.format(self.chain)

    def __str__(self):
        return 'RNK: {}'.format(self.chain)


class DNK(Chain):
    def __init__(self, chain):
        super().__init__(chain)
        self.equal_bases = {
                            'A': 'T',
                            'T': 'A',
                            'G': 'C',
                            'C': 'G'
                            }

    def get_one_base(self, i):
        return (self.chain[i], self.equal_bases[self.chain[i]])

    def __repr__(self):
        return 'DNK: {} || {}'.format(self.chain, self.get_complement_DNK())

    def __str__(self):
        return 'DNK: {} || {}'.format(self.chain, self.get_complement_DNK())
