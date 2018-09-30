# Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

# Example

# For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
# kthLargestElement(nums, k) = 6;
# For nums = [99, 99] and k = 1, the output should be
# kthLargestElement(nums, k) = 99.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer nums

# Guaranteed constraints:
# 1 ≤ nums.length ≤ 105,
# -105 ≤ nums[i] ≤ 105.

# [input] integer k

# Guaranteed constraints:
# 1 ≤ k ≤ nums.length.





class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, key):
        self.heap_list.append(key)
        self.size += 1
        self.perc_up(self.size)

    def perc_up(self, idx):
        while (idx//2):
            if self.heap_list[idx] > self.heap_list[idx//2]:
                self.heap_list[idx], self.heap_list[idx//2] = self.heap_list[idx//2], self.heap_list[idx]
            idx //= 2

    def del_max(self):
        ret = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop(self.size)
        self.size -= 1
        self.perc_down(1)
        return ret

    def perc_down(self, idx):
        while idx * 2 <= self.size:
            max_child = self.max_child_idx(idx)
            if self.heap_list[max_child] > self.heap_list[idx]:
                self.heap_list[max_child], self.heap_list[idx] = self.heap_list[idx], self.heap_list[max_child]
            idx = max_child

    def max_child_idx(self, idx):
        if (idx * 2) +1 > self.size:
            return idx * 2
        if self.heap_list[(idx*2)+1] > self.heap_list[idx*2]:
            return (idx * 2) + 1
        return (idx * 2)

    def has_value(self, value):
        return value in set(self.heap_list)
        
    def get_heap(self):
        print ([x for x in self.heap_list[1:]])
        # for item in self.heap_list[1:]:
        #     yield item

    def build_heap(self, a_list):
        mid = len(a_list)//2
        self.heap_list = [0] + a_list
        self.size = len(a_list)

        while mid:
            self.perc_down(mid)
            mid -= 1
        # for num in a_list:
        #     self.insert(num)

    
if __name__ == "__main__":
    h = BinHeap()
    # h.insert(5)
    # h.insert(3)
    # h.insert(10)
    # # for item in h.get_heap():
    # #     print  (item)
    # h.get_heap()
    # print (h.del_max())
    # print (h.del_max())
    # print (h.del_max())
    a = [7, 6, 5, 4, 3, 2, 1]
    h.build_heap(a)
    k = 2


for i in range(1,k):
    h.del_max()
print (h.del_max())


