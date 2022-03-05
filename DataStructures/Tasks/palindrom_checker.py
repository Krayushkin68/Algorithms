from DataStructures.deque import Deque


def palcheck(str_to_check):
    deque = Deque()
    for char in str_to_check:
        deque.add_rear(char)

    is_pal = True
    while deque.size() > 1 and is_pal:
        if deque.remove_front() != deque.remove_rear():
            is_pal = False
    return is_pal


if __name__ == '__main__':
    print(palcheck("lsdkjfskf"))
    print(palcheck("radar"))
