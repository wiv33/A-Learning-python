from unittest import TestCase

from .string_to_integer_atoi import Solution


class Test(TestCase):
    def test_string_to_integer_atoi(self):
        data = "4193 with words"
        actual = Solution(data).string_to_integer_atoi()
        self.assertEqual(4193, actual)

    def test_string_to_integer_digit(self):
        data = "   -42"
        actual = Solution(data).string_to_integer_atoi()
        self.assertEqual(-42, actual)

    def test_string_to_integer_float(self):
        data = "3.14159"
        actual = Solution(data).string_to_integer_atoi()
        self.assertEqual(3, actual)

    def test_string_to_integer_42(self):
        data = "42"
        actual = Solution(data).string_to_integer_atoi()
        self.assertEqual(42, actual)
