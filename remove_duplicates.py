class Solution:
    def __init__(self):
        self.name = 'henry'

    def removeDuplicates(self, nums):
        idx = 0
        
        for num in nums:
            if idx < 2 or nums[idx-2] < num:
                nums[idx] = num
                idx += 1
        
        return idx

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg = 0
        end = len(nums)-1
        dup = False

        while beg < end:
            check = nums[beg]
            if not dup:
                dup = (check == nums[beg + 1])
                beg += 1

                print(check, dup)
                continue
            else:
                print ('check', check)
                while beg < end and check == nums[beg+1]:
                    nums.pop(beg+1)
                    end -= 1
                dup = False
 
            beg += 1
                 
        print (nums)


    
if __name__ == "__main__":
    s = Solution()
    a = [1,1,1,2,2,3,5,5,5,6,7,7,7,7,8]
    a =[0,0,1,1,1,1,2,3,3]
    print (a)
    s.removeDuplicates(a)
        