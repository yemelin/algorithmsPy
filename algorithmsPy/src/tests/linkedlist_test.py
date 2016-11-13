'''
Created on Nov 13, 2016

@author: vvy
'''
import unittest
from algo.list.linked import LinkedList, Element


class Test(unittest.TestCase):


    def setUp(self):
# Set up some Elements
        self.e1 = Element(1)
        self.e2 = Element(2)
        self.e3 = Element(3)
        self.e4 = Element(4)

# Start setting up a LinkedList
        self.list = LinkedList(self.e1)
        self.list.append(self.e2)
        self.list.append(self.e3)
        

    def tearDown(self):
        pass


    def testList(self):
        self.assertEqual(self.e3, self.list.get_position(3));
        self.list.insert(self.e4, 3);
        self.assertEqual(self.e4, self.list.get_position(3));
        
        self.list.delete(1);
        self.assertEqual(self.e2, self.list.get_position(1));
        self.assertEqual(self.e4, self.list.get_position(2));
        self.assertEqual(self.e3, self.list.get_position(3));


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
