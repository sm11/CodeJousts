def insertBits(n, a, b, k):
    num = format(n, 'b')
    mask = ''

    for i in range(len(num), -1, -1):
        if i not in range(a, b+1):
            mask += '1'
        else:
            mask+= '0'

#     mask = int(mask,2)
#     res = n & mask
#     rep2 = k << a
#     res = res | rep2
     

    return n & int(mask,2) | k << a
