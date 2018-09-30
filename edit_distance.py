import unittest

def rec_edit_distance(str1, str2, cost = 0, memo={}):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    # memo = {}

    tup1 = (str1[:-1], str2)
    tup2 = (str1, str2[:-1])
    tup3 = (str1[:-1], str2[:-1])

    cost = (str1[-1] != str2[-1])
    if tup1 not in memo:
        memo[tup1] = rec_edit_distance(*tup1)
    if tup2 not in memo:
        memo[tup2] = rec_edit_distance(*tup2)
    if tup3 not in memo:
        memo[tup3] = rec_edit_distance(*tup3)

    return min(memo[tup1]+1, memo[tup2]+1, memo[tup3]+cost)


def it_edit_distance(source, target):
    # str1 == source string (written down cols; character per row)
    # str2 == target string (written across; characer per column rows)

    rows = len(source)+1
    cols = len(target)+1

    dist_mat = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(1, rows):
        dist_mat[i][0] = i
    for j in range(1, cols):
        dist_mat[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            cost = (source[row - 1] != target[col - 1])
            # if source[row - 1] ==  target[col - 1]:
            #     cost = 0
            # else:
            #     cost = 1

            dist_mat[row][col] = min(dist_mat[row-1][col] + 1,   # deletion
                                     dist_mat[row][col-1] + 1,   # insertion
                                     dist_mat[row-1][col-1]+ cost)  # substitution

    print()
    for r in range(rows):
        print (dist_mat[r])
    # print (dist_mat)
    print ()
    return dist_mat[-1][-1]



def it_edit_distance_cost (source, target, costs=(1,1,1)):
    """ 
    iterative_levenshtein(s, t) -> ldist
    ldist is the Levenshtein distance between the strings 
    s and t.
    For all i and j, dist[i,j] will contain the Levenshtein 
    distance between the first i characters of s and the 
    first j characters of t
    
    costs: a tuple or a list with three integers (d, i, s)
            where   d defines the costs for a deletion
                    i defines the costs for an insertion and
                    s defines the costs for a substitution
    """

    rows = len(source)+1
    cols = len(target)+1
    dels, ins, subs = costs

    dist_mat = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        dist_mat[i][0] = i * dels
    for j in range(1, cols):
        dist_mat[0][j] = j * ins

    
    for col in range(1, cols):
        for row in range(1, rows):
            cost = 0 if (source[row-1] ==  target[col-1]) else subs

            dist_mat[row][col] = min(dist_mat[row-1][col] + dels,   # deletion
                                     dist_mat[row][col-1] + ins,   # insertion
                                     dist_mat[row-1][col-1]+ cost)  # substitution

    print()
    for r in range(rows):
        print (dist_mat[r])
    # print (dist_mat)
    print ()
    return dist_mat[-1][-1]




def it_edit_distance_weights(source, target, **weight_dict):
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

    w = dict((x, (1,1,1)) for x in string.ascii_lowercase + string.ascii_uppercase)
    if weight_dict:
        w.update(weight_dict)

    dist_mat = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(1, rows):
        dist_mat[row][0] = dist_mat[row-1][0] + w[source[row-1]][0]
    for col in range(1, cols):
        dist_mat[0][col] = dist_mat[0][col-1] + w[target[col-1]][1]

    
    for col in range(1, cols):
        for row in range(1, rows):
            dels = w[source[row-1]][0]
            ins = w[target[col-1]][1]
            subs = max((w[source[row-1]][2], w[target[col-1]][2]))
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
        self.assertEqual(edit_distance('at', 'cat'), 1)
        self.assertEqual(edit_distance('boat', 'got'), 2)
        self.assertEqual(edit_distance('thought', 'sloughs'), 3)


if __name__ == "__main__":
    # unittest.main()
    # print (edit_distance('at', 'cat'))
    # print (edit_distance("Python", "Peithen"))
    # print (ord('a')+ord('b')+ord('g'))

    # print (it_edit_distance('at', 'cat'))
    print ('\n' + '---' * 8 + '\n')
    # print (it_edit_distance_cost('flaw', 'lawn'))
    print(it_edit_distance_weights("abx", 
                            "xya", 
                            x=(3, 2, 8),
                            y=(4, 5, 4),
                            a=(7, 6, 6)) )
    
    
    print(it_edit_distance_weights("at", "cat"))