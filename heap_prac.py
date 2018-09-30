class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.curr_size += 1
        self.perc_up(value)

    def perc_up(self, idx):
        while (idx // 2):
            if self.heap_list[idx] > self.heap_list[idx //2 ]:
                self.heap_list[idx], self.heap_list[idx//2] = self.heap_list[idx//2], self.heap_list[idx]

    def del_max(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        self.perc_down(1)

        return ret_val 

    def perc_down(self, idx):
        while idx * 2 <= self.curr_size:
            max_child = self.max_child(idx)
            if self.heap_list[idx] < self.heap_list[max_child]:
                self.heap_list[idx], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[idx]
            idx = max_child

    def max_child(self, idx):
        if (idx * 2)+1 > self.curr_size:
            return idx*2
        if self.heap_list[idx * 2 ] > self.heap_list[(idx*2)+1]:
            return idx * 2
        return (idx * 2) +1

    def get_max(self):
        return self.heap_list[1]

    def get_size(self):
        return self.curr_size

    def build_heap(self, a_list):
        self.heap_list = [0] + a_list[:]
        self.curr_size = len(a_list)
        mid = len(a_list)//2

        while mid:
            self.perc_down(mid)
            mid -= 1


if __name__ == "__main__":
    a = [5,3,6,7,8,23,4,15,6,7]
    heap = BinaryHeap()
    heap.build_heap(a)
    print (heap.get_max())
    print (heap.del_max())
    print (heap.get_max())