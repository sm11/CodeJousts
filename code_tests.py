import unittest
from sec_max import *

class Tests(unittest.TestCase):
    def test_results(self):
        self.assertEqual(sec_max([-2,-1]), -1)

if __name__== "__main__":
    unittest.main()
    #test = Tests()
    #test.test_results()

