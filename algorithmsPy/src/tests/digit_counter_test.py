'''
Created on Nov 18, 2016

@author: vvy
'''
import unittest
from algo.recursion.digit_counter import count_digits


class Test(unittest.TestCase):


    def test_digit_counter(self):
        self.assertEqual(count_digits(15), 2)
        self.assertEqual(count_digits(105), 3)
        self.assertEqual(count_digits(15105), 5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_digit_counter']
    unittest.main()