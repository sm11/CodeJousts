import unittest


def get_closing_paren(sentence, opening_paren_index):
    open_ = []
    par_dic = {}
    for i, v in enumerate (sentence):
        if v == '(':
            open_.append(i)
        elif v  == ')':
            par_dic[open_.pop()] = i
            
    

    # Find the position of the matching closing parenthesis
    

    return par_dic[opening_paren_index]


















# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)