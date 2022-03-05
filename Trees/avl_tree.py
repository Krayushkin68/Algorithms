from Trees.bin_search_tree import BinarySearchTree, TreeNode


class AVLNode(TreeNode):
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        super(AVLNode, self).__init__(key, val, left, right, parent)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def put(self, key, val):
        if not self.root:
            self.root = AVLNode(key, val)
            self.size += 1
        else:
            cur_node = self.root
            while True:
                if key < cur_node.key:
                    if not cur_node.has_left_child():
                        cur_node.left_child = AVLNode(key, val, parent=cur_node)
                        self.size += 1
                        self.update_balance(cur_node.left_child)
                        break
                    cur_node = cur_node.has_left_child()
                elif key > cur_node.key:
                    if not cur_node.has_right_child():
                        cur_node.right_child = AVLNode(key, val, parent=cur_node)
                        self.size += 1
                        self.update_balance(cur_node.right_child)
                        break
                    cur_node = cur_node.has_right_child()
                else:
                    cur_node.val = val
                    break

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rot_root: AVLNode):
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.has_left_child():
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root: AVLNode):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.has_right_child():
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balanceFactor > 0:
            if node.left_child.rotate_left < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)


if __name__ == '__main__':
    mytree = AVLTree()
    mytree[2] = "at"
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[5] = "orange"
    mytree[6] = "yellow"
