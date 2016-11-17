import unittest

from stack.stack_user import reverse, isBalanced


class MyTestCase(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(['c','b','a'], reverse("abc"))

    def test_isBalanced(self):
        data = [["", True],
        ["abc", True],
        ["[ab[()b]]", True],
        ["(l)c", True],
        ["{[]]", False],
        ["[[()", False],
        ["{][}", False],
        ["{[()}]", False]]

        for test_data in data:
            print 'testing ',test_data[0]
            self.assertEqual(isBalanced(test_data[0]), test_data[1])

if __name__ == '__main__':
    unittest.main()
