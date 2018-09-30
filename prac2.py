def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
        print (res)
    return res

a = [2,3,5,2,3,5]
print (singleNumber(a))
for n in a:
    print (format(n, 'b').zfill(8))