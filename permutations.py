import itertools

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return ["".join (x) for x in list(itertools.product(*nums))]
a =['123','231','312']
print (permute(a))