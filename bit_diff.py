def differentRightmostBit(n, m):
    c = n ^ m
    print (format (n, 'b'))
    print (format (m, 'b'))
    print (format (c, 'b'))
    print (format (-c, 'b'))
    print((-c&c))
    print(format(-c&c, 'b'))

if __name__ == "__main__":
    a = 11
    b = 13
    differentRightmostBit(a, b)