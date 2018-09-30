def coin_cast (val, denoms, nums = []):
    if rem == 0:
        return nums
    sort = sorted(denoms, reverse=True)
    #rem = val
    for idx,s in enumerate(sort):
        if val > s:
            nums.append(s)
            coin_cast(val-s, sort, nums)
        else:
            coin_cast(val, sort[1:], nums)


            

if __name__ == "__main__":
    coin_cast(4, [1,2,3])