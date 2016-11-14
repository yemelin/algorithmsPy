'''
Created on Nov 14, 2016

@author: vvy
'''
import unittest
from algo.list.linkedreversible import LinkedReversible

class Test(unittest.TestCase):


    def setUp(self):
# Start setting up a LinkedList
        self.list = LinkedReversible(1)
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

    def testSizeAndReverse(self):
        '''
        while (self.list.get_position(i))!=None:
            e = self.list.get_position(i)
            i+=1
            print e
        '''
        #print self.list.get_position(position)

        self.assertEqual(3, self.list.size());
        self.list.append(4);

        self.assertEqual(4, self.list.size());
        self.list.delete(4);
        self.assertEqual(3, self.list.size());
        
        
        self.list.reverse();
        self.assertTrue(3 == self.list.get_position(1) and 1==self.list.get_position(3));
#         while (self.list.get_position(i))!=None:
#             e = self.list.get_position(i)
#             i+=1
#             print i,e        
        self.list.insert(3, 2);
        self.assertEqual(4, self.list.size());

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()