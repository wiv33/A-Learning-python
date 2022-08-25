import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        strs = ["h", "e", "l", "l", "o"]
        self.assertListEqual(strs, ["h", "e", "l", "l", "o"])
        Solution(strs).result()
        print(strs)
        self.assertListEqual(strs, ["o", "l", "l", "e", "h"])


if __name__ == '__main__':
    unittest.main()
