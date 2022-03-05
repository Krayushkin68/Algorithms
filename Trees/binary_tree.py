class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left_child = None
        self.right_child = None

    def add_left_child(self, key=None):
        if self.left_child:
            tmp = BinaryTree(key)
            tmp.add_left_child(self.left_child)
            self.left_child = tmp
        else:
            self.left_child = BinaryTree(key)

    def add_right_child(self, key=None):
        if self.right_child:
            tmp = BinaryTree(key)
            tmp.right_child = self.right_child
            self.right_child = tmp
        else:
            self.right_child = BinaryTree(key)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


def build_tree():
    r = BinaryTree('a')
    r.add_left_child('b')
    r.add_right_child('c')
    r.get_left_child().add_right_child('d')
    r.get_right_child().add_left_child('e')
    r.get_right_child().add_right_child('f')
    return r


if __name__ == '__main__':
    tree = build_tree()
