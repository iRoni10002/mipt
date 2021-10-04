class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Some shape {}*{}'.format(self.width, self.height)

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__vertex_number = 3

    def area(self):
        return self.width * self.height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__vertex_number = 4

    def area(self):
        return self.width * self.height


class Mother():
    def __repr__(self):
        return 'This is print of Mother'

class Daughter(Mother):
    def __repr__(self):
        return 'This is print of Daughter'


class Animal():
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __init__(self, name, age, description):
        super().__init__(name, age)
        self.description = description

    def __repr__(self):
        return '''
                This is zebra {}. It is {} years old.
                Some description about it: \n \t {}
               '''.format(self.name, self.age, self.description)

class Dolphin(Animal):
    def __init__(self, name, age, description):
        super().__init__(name, age)
        self.description = description

    def __repr__(self):
        return '''
                This is dolphin {}. It is {} years old.
                Some description about it: \n \t {}
               '''.format(self.name, self.age, self.description)
