from unittest import TestCase

from .longest_palindrome import Solution


class TestSolution(TestCase):
    def test_longest_palindrome(self):
        palindrome = Solution("babad").longest_palindrome()
        self.assertEqual("bab", palindrome)
