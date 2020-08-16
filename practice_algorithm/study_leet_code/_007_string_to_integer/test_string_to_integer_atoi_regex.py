import re
from unittest import TestCase

from .string_to_integer_atoi_regex import Solution


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

    def test_print_re(self):
        s = "-+23412"
        search = re.search(r'([-+]{2})|[a-zA-Z]', s)
        print(search)
        self.assertTrue(search)

    def test_available_eval(self):
        s = "+00000000032342"
        search = re.search(r'[-+]', s)
        print(search)
        self.assertTrue(search)

        s = "-028328032"
        search = re.search(r'[-+]', s)
        print(search)
        self.assertTrue(search)

        s = "  +-028328032"
        search = re.search(r'[-+[^a-zA-Z]]', s)
        print(search)
        self.assertFalse(search)

    def test_re_sub_remove_zero(self):
        s = "-0000000000012345600000"
        sub = re.sub(r'(?<=[-+])0*[^1-9]', "", s)
        self.assertEqual("-12345600000", sub)

        s = "+000000000001234560"
        sub = re.sub(r'(?<=[-+])0*[^1-9]', "", s)
        self.assertEqual("+1234560", sub)

    def test_words(self):
        atoi = Solution("words and 987").string_to_integer_atoi()
        print(atoi)

    def test_000000000000(self):
        actual = Solution("    0000000000000   ").string_to_integer_atoi()
        print(actual)

    def test_eval_0000000000(self):
        s = "   -42"
        actual = Solution(s).string_to_integer_atoi()
        self.assertEqual(-42, actual)

    def test_eval_plus_and_minus(self):
        s = "+-2"
        actual = Solution(s).string_to_integer_atoi()
        self.assertEqual(0, actual)

    def test_eval_010(self):
        s = "010"
        actual = Solution(s).string_to_integer_atoi()
        self.assertEqual(10, actual)

    def test_eval_004500(self):
        s = "     +004500"
        actual = Solution(s).string_to_integer_atoi()
        self.assertEqual(4500, actual)

    def test_eval_what_the(self):
        s = "  -0012a42"
        actual = Solution(s).string_to_integer_atoi()
        self.assertEqual(-12, actual)
