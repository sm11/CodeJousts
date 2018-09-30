import heapq
# from heapq import heappop

def kthLargestElement(nums, k):
    heapq.heapify(nums)    
    for i in range(len(nums) - k):
        heapq.heappop(nums)
    return nums[0]



if __name__ == "__main__":
    nums = [7, 6, 5, 4, 3, 2, 1]
    # k = 2
    # print (kthLargestElement(nums, k))
    largest = (heapq.nlargest(2, nums)[-1])
    print (largest)
