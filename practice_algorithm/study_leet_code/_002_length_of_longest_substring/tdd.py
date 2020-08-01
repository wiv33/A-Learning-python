import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_final(self):
        actual = Solution().lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(expected, actual)

    def test_string_split(self):
        input_data = "abcabcbb"
        for i, s in enumerate(input_data):
            input_data[i]
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
