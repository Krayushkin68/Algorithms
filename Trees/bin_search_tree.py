class TreeNode:
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __repr__(self):
        return str(self.key)

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_child(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.findSuccessor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        try:
            self._get(key)
            return True
        except KeyError:
            return False

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
            self.size += 1
        else:
            cur_node = self.root
            while True:
                if key < cur_node.key:
                    if not cur_node.has_left_child():
                        cur_node.left_child = TreeNode(key, val, parent=cur_node)
                        self.size += 1
                        break
                    cur_node = cur_node.has_left_child()
                elif key > cur_node.key:
                    if not cur_node.has_right_child():
                        cur_node.right_child = TreeNode(key, val, parent=cur_node)
                        self.size += 1
                        break
                    cur_node = cur_node.has_right_child()
                else:
                    cur_node.val = val
                    break

    def _get(self, key):
        if not self.root:
            raise KeyError

        cur_node = self.root
        while True:
            if key < cur_node.key:
                if not cur_node.has_left_child():
                    raise KeyError
                cur_node = cur_node.has_left_child()
            elif key > cur_node.key:
                if not cur_node.has_right_child():
                    raise KeyError
                cur_node = cur_node.has_right_child()
            else:
                return cur_node

    def get(self, key):
        node = self._get(key)
        return node.val

    def delete(self, key):
        node = self._get(key)
        self.size -= 1
        if node.is_leaf():
            if not node.is_root():
                if node.is_left_child():
                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
            else:
                self.root = None
        elif node.has_both_child():
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.val = succ.val
        else:
            if node.has_right_child():
                if node.is_right_child():
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                elif node.is_left_child():
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                else:
                    self.root = node.right_child
            else:
                if not node.is_root():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                else:
                    self.root = node.left_child


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[5] = "orange"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    mytree.delete(5)
