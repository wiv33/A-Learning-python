from unittest import TestCase

from .palindrome_number import Solution


class TestSolution(TestCase):
    def test_palindrome_number(self):
        self.assertTrue(Solution().isPalindrome(12121))

    def test_palindrome_10101(self):
        self.assertTrue(Solution().isPalindrome(10101))

    def test_palindrome_number_0(self):
        self.assertFalse(Solution().isPalindrome(1213))

    def test_palindrome_number_22(self):
        self.assertTrue(Solution().isPalindrome(22))
