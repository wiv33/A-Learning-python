import unittest

from .find_max import find_max, find_max_index


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(65, find_max([5, 6, 3, 6, 1, 2, 5, 7, 8, 10, 52, 65, 45]))
        self.assertEqual(33, find_max([33, 5, 6, 3, 6, 1, 2, 5, 7, 8, 10, ]))

    def test_find_max_index(self):
        self.assertEqual(2, find_max_index([17, 24, 33, 5, 6, 3, 6, 1, 2, 5, 7, 8, 10, ]))

    if __name__ == '__main__':
        unittest.main()
