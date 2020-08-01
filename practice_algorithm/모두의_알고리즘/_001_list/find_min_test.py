import unittest

from .find_min import find_min


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(2, find_min([12, 52, 62, 7, 5, 3, 7, 9, 12, 5, 2, 8, 11]))


if __name__ == '__main__':
    unittest.main()
