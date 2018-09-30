import unittest

def ascii_deletion_distance(source, target):
    rows = len(source)+1
    cols = len(target)+1

    dist = [[0 for j in range(cols)] for i in range(rows)]

    # for i in range(1, rows):
    #     dist[i][0] = i
    
    # for j in range(1,cols):
    #     dist[0][j] = j
  
    for row in range(rows):
        for col in range(cols):
            if row == 0:
                # print(target[:col])
                dist[row][col] = sum([ord(c) for c in target[:col]])       #sum(bytearray(target[:col], 'utf8'))  
            elif not col:
                dist[row][col]= sum([ord(c) for c in source[:row]])  #sum(bytearray(source[:row], 'utf8'))  
            elif source[row-1] == target[col-1]:
                dist[row][col] = dist[row-1][col-1]
            else:
                src_del = ord(source[row-1])
                tar_del = ord(target[col-1])
                src_tar_del = src_del + tar_del
                dist[row][col] = min(dist[row-1][col-1]+src_tar_del, 
                                    dist[row-1][col] + src_del,
                                    dist[row][col-1]+tar_del)
    print()
    for r in range(rows):
        print (dist[r])
    print ()

    return dist[-1][-1]

def delete_distance(s1, s2):
    m = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0:
                # if s2[:j] != '':
                #     print ('r', bytearray(s2[:j], 'utf8'), int(bytearray(s2[:j], 'utf8').hex(), 16), sum(bytearray(s2[:j], 'utf8')))
                m[i][j] = sum(bytearray(s2[:j], 'utf8'))
            elif j == 0:
                # if s1[:i] != '':
                #     print ('c', bytearray(s1[:i], 'utf8'), int(bytearray(s1[:i], 'utf8').hex(), 16))
                m[i][j] = sum(bytearray(s1[:i], 'utf8'))
            elif s1[i-1] == s2[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                s1del = ord(s1[i-1])
                s2del = ord(s2[j-1])
                s1s2del = s1del + s2del
                m[i][j] = min(m[i-1][j-1] + s1s2del, m[i-1][j] + s1del, m[i][j-1] + s2del)
    
    print()
    for r in range(len(s1)+1):
        print (m[r])
    print ()
    
    
    return m[len(s1)][len(s2)]


def delete_distance_weights(source, target, **weight_dict):
    """ 
    iterative_levenshtein(s, t) -> ldist
    ldist is the Levenshtein distance between the strings 
    s and t.
    For all i and j, dist[i,j] will contain the Levenshtein 
    distance between the first i characters of s and the 
    first j characters of t
    
    weight_dict: keyword parameters setting the costs for characters,
                     the default value for a character will be 1
    """
    import string

    rows = len(source)+1
    cols = len(target)+1

    w = dict((x, ord(x)) for x in string.ascii_lowercase + string.ascii_uppercase)
    if weight_dict:
        w.update(weight_dict)

    dist_mat = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(1, rows):
        dist_mat[row][0] = dist_mat[row-1][0] + w[source[row-1]]
    for col in range(1, cols):
        dist_mat[0][col] = dist_mat[0][col-1] + w[target[col-1]]

    
    for col in range(1, cols):
        for row in range(1, rows):
            dels = w[source[row-1]]
            ins = w[target[col-1]]
            subs = (w[source[row-1]] + w[target[col-1]])
            if source[row-1] ==  target[col-1]:
                cost = 0
            else:
                cost = subs

            dist_mat[row][col] = min(dist_mat[row-1][col] + dels,   # deletion
                                     dist_mat[row][col-1] + ins,   # insertion
                                     dist_mat[row-1][col-1]+ cost)  # substitution

    print()
    for r in range(rows):
        print (dist_mat[r])
    # print (dist_mat)
    print ()
    return dist_mat[-1][-1]



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_deletion_distance('at', 'cat'), 99)
        self.assertEqual(ascii_deletion_distance('boat',  'got'), 298)
        self.assertEqual(ascii_deletion_distance('thought' ,  'sloughs'), 674)



if __name__ == "__main__":
    # unittest.main()
    print (ascii_deletion_distance('at', 'cat'))
    # print (delete_distance('at', 'cat'),)
    # print (ord('a')+ord('b')+ord('g'))
    # print (bytearray(b''))
    # print (type(str.encode('c')))
    # print (int(str.encode('c').hex(), 16))
    # print (ord('t'))
    # print(256 - ord('c'))
    
    