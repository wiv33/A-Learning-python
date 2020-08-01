import unittest

from .my_factorial import factorial


class MyTestCase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(120, factorial(5))
        self.assertEqual(24, factorial(4))


if __name__ == '__main__':
    unittest.main()
