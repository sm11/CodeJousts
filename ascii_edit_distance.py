# The deletion distance between two strings is the minimum sum of ASCII values of 
# characters that you need to delete in the two strings in order to have the same 
# string. The deletion distance between cat and at is 99, because you can just 
# delete the first character of cat and the ASCII value of 'c' is 99.
# The deletion distance between cat and bat is 98 + 99, because you need 
# to delete the first character of both words. Of course, the deletion distance 
# between two strings can't be greater than the sum of their total ASCII values, 
# because you can always just delete both of the strings entirely. 
# Implement an efficient function to find the deletion distance between two strings.
#  You can refer to the Wikipedia article on the algorithm for edit distance 
# if you want to. The algorithm there is not quite the same as the algorithm 
# required here, but it's similar.

import unittest

def ascii_deletion_distance(str1, str2, l=[], cost=0):
    if not str1:
        return len(str2)
        # return list(str2)
    if not str2:
        return len(str1)
        # return list(str1)

    # l1 = list(str1).sort()
    # l2 = list(str2).sort()
    cost = (str1[-1] != str2[-1])
    if str1[-1] != str2[-1]:
        cost = ord(str1[-1]) + ord(str2[-1])

    res =  min(ascii_deletion_distance(str1[:-1], str2, l + [str2[:-1]] )+1, 
                ascii_deletion_distance(str1, str2[:-1], l+[str1[:-1]])+1, 
                ascii_deletion_distance(str1[:-1], str2[:-1], l+[str1[:-1],str1[:-1]])+cost)
    # print (set(l))
    return res





class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_deletion_distance('at', 'cat'), 99)
        self.assertEqual(ascii_deletion_distance('boat',  'got'), 298)
        self.assertEqual(ascii_deletion_distance('thought' ,  'sloughs'), 674)



if __name__ == "__main__":
    # unittest.main()
    print (ascii_deletion_distance('at', 'cat'),)
    # print (ord('a')+ord('b')+ord('g'))
    
    
    