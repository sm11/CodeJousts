import unittest

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('less')
    
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_k = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_k = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2, current * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)
        lowest_product_of_2 = min(lowest_product_of_2, current * highest, current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)
        
    return highest_product_of_3

product = lambda arr: reduce(lambda x,y: x*y, arr, 1)

def highest_product_of_3(array_of_ints):
	n=3
	if len(array_of_ints) < n: 
		raise Exception("Less than %d items!" % n)

	highest_product = [product(array_of_ints[:i]) for i in range(2, n+1)]
	lowest_product = [product(array_of_ints[:i]) for i in range(2, n+1)]

	highest_product.insert(0, max(array_of_ints[:n-1]))
	lowest_product.insert(0, min(array_of_ints[:n-1]))

	for current in array_of_ints[n-1:]:

		for i in range(len(highest_product)-1, 0, -1):

			highest_product[i] = max(
				highest_product[i],
				current * highest_product[i-1],
				current * lowest_product[i-1],
			)

			lowest_product[i] = min(
				lowest_product[i],
				current * highest_product[i-1],
				current * lowest_product[i-1],
			)

		highest_product[0] = max(highest_product[0], current)
		lowest_product[0] = min(lowest_product[0], current)

	return highest_product[-1]
        
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