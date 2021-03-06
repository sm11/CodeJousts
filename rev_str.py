import unittest
def rev_str(word, beg, end):
    while beg < end:
        word[beg], word[end] = word[end], word[beg]
        beg += 1
        end -= 1

def reverse_words(message):
    # Decode the message by reversing the words
  
    rev_str(message,0,len(message)-1)
  
    beg = 0
    for ind, val in enumerate(message):
        if val == " ":
            rev_str(message, beg, ind-1)
            beg = ind+1
    rev_str(message, beg, len(message)-1  )  

    return message


















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)