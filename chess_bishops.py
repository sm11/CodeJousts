# In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

# Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

# Example

# For bishop1 = "d7" and bishop2 = "f5", the output should be
# bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].



# For bishop1 = "d8" and bishop2 = "b5", the output should be
# bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].

# The bishops don't belong to the same diagonal, so they don't move.


# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string bishop1

# Coordinates of the first bishop in chess notation.

# [input] string bishop2

# Coordinates of the second bishop in the same notation.

# [output] array.string

# Coordinates of the bishops in lexicographical order after they check the diagonals they stand on.



def moveupleft(let, num):
    while ord('a') < let  and num < 8:
        let -= 1
        num += 1
    return (chr(let)+str(num))

def moveupright(let,num):
    while ord('a') < let and num > 1:
        let -= 1
        num -= 1
    return (chr(let)+str(num))

def movedownleft(let, num):
    while ord('h') > let  and num < 8:
        let += 1
        num += 1
    return (chr(let)+str(num))

def movedownright(let, num):
    while ord('h') > let and num > 1:
        let += 1
        num -= 1
    return (chr(let)+str(num))


def moveupleft(let, num):
    while ord('a') < let  and num < 8:
        let -= 1
        num += 1
    return (chr(let)+str(num))

def moveupright(let,num):
    while ord('a') < let and num > 1:
        let -= 1
        num -= 1
    return (chr(let)+str(num))

def movedownleft(let, num):
    while ord('h') > let and num < 8:
        let += 1
        num += 1
    return (chr(let)+str(num))

def movedownright(let, num):
    while ord('h') > let and num > 1:
        let += 1
        num -= 1
    return (chr(let)+str(num))


def bishopDiagonal(bishop1, bishop2):
    a0 = ord(bishop1[0])
    b0 = ord(bishop2[0]) 
    a1 = int(bishop1[1])
    b1 = int(bishop2[1])
    
    new1 = bishop1
    new2 = bishop2
    
    
    if  abs(a0 - b0) == abs(a1 - b1) :
        if a0 < b0:
            if a1 < b1:
                new1 = movedownleft(a0,a1)
                new2 = moveupright(b0,b1)
            else:
                new1 = moveupleft(a0,a1)
                new2 = movedownright(b0,b1)
        else:
            if a1 < b1:
                new1 = movedownright(a0,a1)
                new2 = moveupleft(b0,b1)
            else:
                new1 = moveupright(a0,a1)
                new2 = movedownleft(b0,b1)
    
    if new1 < new2:
        return [new1, new2]
    return [new2, new1]


