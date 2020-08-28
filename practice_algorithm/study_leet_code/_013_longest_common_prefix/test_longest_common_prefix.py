from unittest import TestCase

from .longest_common_prefix import Solution


class TestSolution(TestCase):
    def test_longest_common_prefix(self):
        actual = Solution().longestCommonPrefix(["flower", "flow", "flight"])
        self.assertEqual("fl", actual)


class TestSolution(TestCase):
    def test_longest_common_prefix_2(self):
        actual = Solution().longestCommonPrefix_2(["flower", "flow", "flight"])
        self.assertEqual("fl", actual)
