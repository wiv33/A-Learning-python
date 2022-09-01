import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("ball",
                         Solution('Bob hit a ball, the hit BALL flew far after it was hit.',
                                  ['hit']).result())


if __name__ == '__main__':
    unittest.main()
