def secondRightmostZeroBit(n):
    #return (((((n + 1) | n) + 1) | n) - n)
    a = (n + 1) | n
    b = (a + 1) | n
    print (n, format(n, 'b'))
    print (n+1, format(n+1, 'b'))
    print (a, format(a, 'b'))
    print (b, format(b, 'b'))
    print ((b - n), format((b-n), 'b'))
    print ("-"*8)
    print (format(int('10101010101010101010101010101010', 2), 'x'))
    print (format(int('01010101010101010101010101010101', 2), 'x'))
    
if __name__ == "__main__":
    n = 1073741824
    secondRightmostZeroBit(n)
    n = 37
    secondRightmostZeroBit(n)
#Output:2