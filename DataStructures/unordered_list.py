class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node

    def set_data(self, data):
        self.data = data


class UnorderedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return '[]'
        else:
            cur_node = self.head
            result = f'[{cur_node.data}'
            while cur_node.next:
                cur_node = cur_node.next
                result += f', {cur_node.data}'
            result += ']'
            return result

    def remove(self, item):
        if not self.head:
            return False
        else:
            if self.head.data == item:
                self.head = self.head.next
                return True
            prev_node = self.head
            while prev_node.next:
                next_node = prev_node.next
                if next_node.data == item:
                    prev_node.next = next_node.next
                    return True
                prev_node = next_node
            return False

    def search(self, item):
        if self.index(item) != -1:
            return True
        else:
            return False

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def size(self):
        if not self.head:
            return 0
        else:
            cur_node = self.head
            counter = 1
            while cur_node.next:
                cur_node = cur_node.next
                counter += 1
            return counter

    def append(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.set_next(Node(item))

    def index(self, item):
        if not self.head:
            return -1
        else:
            if self.head.data == item:
                return 0
            cur_node = self.head
            index = 1
            while cur_node.next:
                cur_node = cur_node.next
                if cur_node.data == item:
                    return index
                index += 1
            return -1

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise Exception('Pos is out of bounds')

        if pos == 0:
            new_node = Node(item)
            new_node.set_next(self.head)
            self.head = new_node
        else:
            cur_node = self.head
            for _ in range(pos - 1):
                cur_node = cur_node.next

            left_node = cur_node
            right_node = left_node.next
            new_node = Node(item)
            left_node.set_next(new_node)
            if right_node:
                new_node.set_next(right_node)

    def pop(self, pos=-1):
        if (pos < 0 and pos != -1) or pos >= self.size():
            raise Exception('List is empty')

        if pos == -1:
            pos = self.size() - 1

        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            prev_node = self.head
            for _ in range(pos - 1):
                prev_node = prev_node.next

            del_node = prev_node.next
            data = del_node.data
            right_node = del_node.next
            prev_node.set_next(right_node)
            return data


if __name__ == '__main__':
    lst = UnorderedList()
    lst.append(12)
    lst.append(16)
    lst.append(88)
    lst.append('dog')
    lst.append(False)
    lst.append('reverse')
