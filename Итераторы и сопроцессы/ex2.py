class BinTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_value(self):
        return self.value


class BinTree():
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.length = 1
        else:
            current = self.head
            while True:
                if node.get_value() == current.get_value():
                    break
                elif node.get_value() < current.get_value():
                    #check left child
                    if current.get_left_child() is None:
                        current.set_left_child(node)
                        break
                    else:
                        #if node has left child
                        current = current.get_left_child()
                else:
                    #check right child
                    if current.get_right_child() is None:
                        current.set_right_child(node)
                        break
                    else:
                        #if node has right child
                        current = current.get_right_child()
            self.length += 1

    def __iter__(self):
        node = self.head
        stack = []
        result = []
        while node or stack:
            while node:
                stack.append(node)
                result.append(node)
                node = node.get_left_child()
            if stack:
                node = stack.pop()
                node = node.get_right_child()
        return iter(result)


nodes = [BinTreeNode(node) for node in [8, 4, 10, 2, 6, 3, 7]]
tree = BinTree()
for i in nodes:
    tree.add_node(i)

for i in tree:
    print(i.get_value())
