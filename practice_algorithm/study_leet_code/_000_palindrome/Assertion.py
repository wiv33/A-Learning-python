import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, Solution("A man, a plan, a canal: Panama").result())
        self.assertEqual(False, Solution("race a car").result())


if __name__ == '__main__':
    unittest.main()
