'''
Created on Nov 15, 2016

@author: vvy
'''
import unittest
from algo.recursion.fib import fib, dumbFibRec, recFibNoMemo, recFibMemo


class Test(unittest.TestCase):


#     @classmethod
    def setUp(self):
#        super(Test, cls).setUpClass()(self):
        self.params = [[0,0],
                [1,1l],
                [2,1l],
                [5,5l],
                [6,8l],
                [8,21l]]
        self.functions = [fib, dumbFibRec, recFibNoMemo, recFibMemo]
        pass


    def tearDown(self):
        pass


    def testFibs(self):
        for f in self.functions:
            print f
            for param in self.params:
                self.assertEqual(param[1], f(param[0]))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()