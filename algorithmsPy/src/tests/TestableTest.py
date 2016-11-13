'''
Created on Nov 13, 2016

@author: vvy
'''
import unittest
import algo.testable.testable as t

#trying to undestand unit testing in python
class Test(unittest.TestCase):


    def testName(self):
        self.assertEqual(5, t.identity(5), "identity fail")
        self.assertNotEqual(5, t.identity(4), "identity fail")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()