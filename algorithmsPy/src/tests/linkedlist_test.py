'''
Created on Nov 13, 2016

@author: vvy
'''
import unittest
from algo.list.linked import LinkedList


class Test(unittest.TestCase):


    def setUp(self):
# Start setting up a LinkedList
        self.list = LinkedList(1)
        self.list.append(2)
        self.list.append(3)
        

    def tearDown(self):
        pass


    def testList(self):
        self.assertEqual(3, self.list.get_position(3));
        self.list.insert(4, 3);
        self.assertEqual(4, self.list.get_position(3));
        
        self.list.delete(1);
        self.assertEqual(2, self.list.get_position(1));
        self.assertEqual(4, self.list.get_position(2));
        self.assertEqual(3, self.list.get_position(3));


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
