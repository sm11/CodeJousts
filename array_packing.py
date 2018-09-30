def arrayPacking(a):
    return sum([a[i] << i*8 for i in range(len(a))])

def arrayPacking(a):
    out = 0
    for i in range(len(a)):
        out += a[i] << 8*i
    return out

def arrayPacking(a):
    arr = []
    for i in a[::-1]:
        arr.append(format(i, 'b').zfill(8)) 
    form = "".join(x for x in arr)
    return (int(form, 2))