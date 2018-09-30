import unittest

def rec_perm(rem, cases, seen):
    if rem == '':
        return cases.add(seen)      
    for idx,val in enumerate(rem):
        rec_perm(rem[:idx] + rem[idx+1:], cases, seen+val)


def get_permutations(string):
    # Generate all permutations of the input string
    
    cases = set()
    rec_perm(string, cases, seen='')
    return cases


def get_permutations_1(string):
    if len(string) < 2:
        return set([string])
    case = set()
    for word in get_permutations(string[:-1]):
        for i in range(len(string)):
            case.add(word[:i] + string[-1] + word[i:])
    return case

# def get_permutations(word):
    
#     if len(word) < 2:
#         return set([word])

#     case = set()
#     for idx, val in enumerate(word):
#         case.update(get_permutations(str(word[:idx]+word[idx+1:])))
#         for w in set(case):
#             for i,v in enumerate(w):
#                 if val not in w:
#                     case.add(w[:i]+val+w[i:])
#     return set([x for x in case if len(x) == len(word)])






































#     # Generate all permutations of the input string
#     res = set()
#     recPermute('', string, res)
#     return res

# def recPermute(seen, rem, res):
#     if rem == '':
#         res.add(seen)
#         return
#     for i in range(len(rem)):
#         recPermute(seen+rem[i], rem[0:i]+rem[i+1:], res)
    
        



# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)