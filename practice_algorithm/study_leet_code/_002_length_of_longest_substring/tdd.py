import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_final(self):
        actual = Solution().lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(expected, actual)

    def test_string_split(self):
        input_data = "abcabcbb"
        for s in input_data:
            print(s)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
