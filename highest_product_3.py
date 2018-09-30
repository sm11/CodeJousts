import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        raise ValueError('Number of integers is less than 3')
        
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_3 = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]
    highest_2 = list_of_ints[0]*list_of_ints[1]
    lowest_2 = list_of_ints[0]*list_of_ints[1]
      

    for idx, current in enumerate(list_of_ints[2:]):
        highest_3 = max(highest_3, highest_2*current, lowest_2*current)
        highest_2 = max(highest_2, highest*current, lowest*current)
        lowest_2 = min(lowest_2, highest*current, lowest*current)
        highest = max(highest, current)
        lowest = min(lowest, current)
    
    return highest_3
        
    
    # Time Complexity nlogn
    # sort = sorted(list_of_ints)
    # return max(sort[0]*sort[1]*sort[-1], sort[-3]*sort[-2]*sort[-1])
   

        
    


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)