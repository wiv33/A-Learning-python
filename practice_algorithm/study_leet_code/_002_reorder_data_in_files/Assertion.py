import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        expected = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        self.assertListEqual(expected, Solution(logs).result())  # add assertion here


if __name__ == '__main__':
    unittest.main()
