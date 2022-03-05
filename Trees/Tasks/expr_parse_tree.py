import operator

from DataStructures.stack import Stack
from Trees.binary_tree import BinaryTree


def build_parse_tree(expression):
    expression = expression.split()
    tree = BinaryTree()
    nodes = Stack()
    nodes.push(tree)
    cur_node = tree

    for el in expression:
        if el == '(':
            nodes.push(cur_node)
            cur_node.add_left_child()
            cur_node = cur_node.get_left_child()
        elif el in ('+', '-', '/', '*'):
            cur_node.set_key(el)
            nodes.push(cur_node)
            cur_node.add_right_child()
            cur_node = cur_node.get_right_child()
        elif el == ')':
            cur_node = nodes.pop()
        else:
            cur_node.set_key(int(el))
            cur_node = nodes.pop()
    return tree


def evaluate_parse_tree(tree: BinaryTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        func = opers[tree.get_key()]
        return func(evaluate_parse_tree(left), evaluate_parse_tree(right))
    else:
        return tree.get_key()


if __name__ == '__main__':
    parse_tree = build_parse_tree('( 3 + ( ( 44 * 5 ) / ( 26 + 8 ) ) )')
    parse_tree.preorder()
    print(evaluate_parse_tree(parse_tree))
