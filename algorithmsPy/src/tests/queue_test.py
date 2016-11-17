import unittest

from algo.queue.queue import MinMaxQueue
from algo.queue.stacked_queue import DualStackQueue


class MyTestCase(unittest.TestCase):

    def test_something(self):
        q = MinMaxQueue()
        q.enqueue(4)
        q.enqueue(3)
        q.enqueue(2)
        q.enqueue(2)

        self.assertEqual(q.min(), 2)
        self.assertEqual(q.max(), 4)

        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.max(), 3)


    def test_dual_stack(self):
        q = DualStackQueue()
        q.enqueue(4);
        self.assertTrue(1==q.size());
        self.assertTrue(4==q.dequeue());
        q.enqueue(4);
        q.enqueue(3);
        q.enqueue(2);
        self.assertTrue(4==q.dequeue());
        
        
if __name__ == '__main__':
    unittest.main()
