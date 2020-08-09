from unittest import TestCase

from .longest_palindrome import Solution
from .solution_ import SolutionOther


class TestSolution(TestCase):
    def test_longest_palindrome(self):
        palindrome = Solution("babad").longest_palindrome()
        self.assertEqual("bab", palindrome)

    def test_longest_other(self):
        actual = SolutionOther().sol("babad")
        self.assertEqual("bab", actual)

        SolutionOther().sol("ddaba")
