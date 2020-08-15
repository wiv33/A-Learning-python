import re
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

    def test_string_to_integer_negative_and_float(self):
        actual = Solution("-91283472332").string_to_integer_atoi()
        self.assertEqual(-2147483648, actual)

    def test_string_to_calculate(self):
        actual = Solution("+").string_to_integer_atoi()
        self.assertEqual(0, actual)

    def test_string_to_00000000000(self):
        actual = Solution("  0000000000012345678").string_to_integer_atoi()
        self.assertEqual(12345678, actual)

    def test_string_to_minus00000000000(self):
        actual = Solution("-000000000000001").string_to_integer_atoi()
        self.assertEqual(-1, actual)

    def test_calculate(self):
        s = "       +-02112"
        self.assertEqual((0, 2), re.search(r'[\W]{2}', s.lstrip()).span(0))

    def test_should_be_not_alpha(self):
        s = "-f010231"
        self.assertFalse(s.isalpha())
        self.assertFalse(s.isdigit())
        self.assertFalse(s.isnumeric())
        self.assertFalse(s.isalnum())

    def test_should_be_alpha(self):
        s = "fwokejo"
        self.assertTrue(s.isalpha())
        self.assertTrue("dfef212412".isalnum())
