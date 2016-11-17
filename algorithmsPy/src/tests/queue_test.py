import unittest

from queue.queue import MinMaxQueue


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


if __name__ == '__main__':
    unittest.main()
