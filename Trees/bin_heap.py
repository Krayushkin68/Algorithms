class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def __repr__(self):
        return self.heap_list.__str__()

    def insert(self, el):
        self.heap_list.append(el)
        self.size += 1
        self.perc_up(self.size)

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                i //= 2
            else:
                break

    def perc_down(self, i):
        while i * 2 <= self.size:
            if i * 2 + 1 <= self.size and self.heap_list[i * 2 + 1] < self.heap_list[2 * i]:
                mc = 2 * i + 1
            else:
                mc = 2 * i

            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
                i = mc
            else:
                break

    def del_min(self):
        if self.size == 0:
            return False
        min_el = self.heap_list[1]
        self.heap_list[-1], self.heap_list[1] = self.heap_list[1], self.heap_list[-1]
        self.heap_list.pop()
        self.size -= 1
        self.perc_down(1)
        return min_el

    def build_heap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heap_list = [0] + alist
        while i > 0:
            self.perc_down(i)
            i -= 1


if __name__ == '__main__':
    mh = BinHeap()
    mh.build_heap([9, 2, 5, 1, 3])
    mh.insert(4)
    mh.del_min()
