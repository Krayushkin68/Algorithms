from Trees.bin_heap import BinHeap
from random import randint


def sort(alist):
    if not alist:
        return alist

    mh = BinHeap()
    mh.build_heap(alist)

    sorted_list = []
    for _ in range(len(alist)):
        sorted_list.append(mh.del_min())
    return sorted_list


if __name__ == '__main__':
    test = [randint(0, 100) for _ in range(20)]
    print(sort(test))
