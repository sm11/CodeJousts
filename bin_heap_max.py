# BinaryHeap() creates a new, empty, binary heap.
# insert(k) adds a new item to the heap.
# findMin() returns the item with the minimum key value, leaving item in the heap.
# delMin() returns the item with the minimum key value, removing the item from the heap.
# isEmpty() returns true if the heap is empty, false otherwise.
# size() returns the number of items in the heap.
# buildHeap(list) builds a new heap from a list of keys.



class BinaryHeap():
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.curr_size += 1
        self.perc_up(self.curr_size)


    def perc_up(self, idx):
        while idx//2:
            if self.heap_list[idx] > self.heap_list[idx//2]:
                self.heap_list[idx], self.heap_list[idx//2] = self.heap_list[idx//2], self.heap_list[idx]
            idx //= 2

    def del_max(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        self.heap_list.pop()
        self.perc_down(1)

        return ret_val


    def perc_down(self, idx):
        while (idx * 2 ) <= self.curr_size:
            max_child = self.max_child(idx)
            if self.heap_list[idx] < self.heap_list[max_child]:
                self.heap_list[idx], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[idx]
            idx = max_child
    

    def max_child(self, idx):
        if (idx * 2)+1 > self.curr_size:
            return idx * 2
        if self.heap_list[idx * 2] > self.heap_list[idx*2+1]:
            return idx * 2
        return (idx * 2) + 1

    def get_max(self):
        return self.heap_list[1]

    def is_empty(self):
        return self.curr_size == 0

    def size(self):
        return self.curr_size

    def build_heap(self, a_list):
        mid =len(a_list)//2
        self.curr_size = len(a_list)
        self.heap_list = [0] + a_list[:]

        while (mid):
            self.perc_down(mid)
            mid -= 1

if __name__ == "__main__":
    a = [10,5,8,3,7,4,2,9, 43, 22, 50, 1]
    heap = BinaryHeap()
    heap.build_heap(a)
    print (heap.get_max())
    print (heap.del_max())
    print (heap.get_max())