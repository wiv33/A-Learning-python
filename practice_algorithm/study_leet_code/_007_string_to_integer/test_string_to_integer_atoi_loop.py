from unittest import TestCase

from .string_to_integer_atoi_loop import Solution


class TestSolution(TestCase):
    def test_string_to_integer_atoi_loop(self):
        actual = Solution("-00042").string_to_integer_atoi_loop()
        self.assertEqual(-42, actual)

    def test_4193_with_words(self):
        actual = Solution("4193 with words").string_to_integer_atoi_loop()
        self.assertEqual(4193, actual)

    def test_start_words(self):
        actual = Solution("words 4193 with").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_minus_42(self):
        data = "   -42"
        actual = Solution(data).string_to_integer_atoi_loop()
        self.assertEqual(-42, actual)

    def test_string_to_integer_negative_and_float(self):
        actual = Solution("-91283472332").string_to_integer_atoi_loop()
        self.assertEqual(-2147483648, actual)

    def test_float(self):
        actual = Solution("3.14159").string_to_integer_atoi_loop()
        self.assertEqual(3, actual)

    def test_float_dot_one(self):
        actual = Solution(".1").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_decimal(self):
        actual = Solution("  0000000000012345678").string_to_integer_atoi_loop()
        self.assertEqual(12345678, actual)

    def test_zero(self):
        actual = Solution("    0000000000000   ").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_empty(self):
        actual = Solution(" ").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_stop_in_word(self):
        actual = Solution("  -0012a42").string_to_integer_atoi_loop()
        self.assertEqual(-12, actual)

    def test_stop_in_word_acc_zero(self):
        actual = Solution("    +0a32").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_max_integer(self):
        actual = Solution("20000000000000000000").string_to_integer_atoi_loop()
        self.assertEqual(2147483647, actual)

    def test_score(self):
        actual = Solution("0-1").string_to_integer_atoi_loop()
        self.assertEqual(0, actual)

    def test_minus_5_minus(self):
        actual = Solution("-5-").string_to_integer_atoi_loop()
        self.assertEqual(-5, actual)
        self.fail()

    def test_mix_plus_minus_nums(self):
        actual = Solution("-13+8").string_to_integer_atoi_loop()
        self.assertEqual(-13, actual)
        self.fail()

    def test_eval(self):
        eval1 = eval("  0000000000012345678")
        print(eval1)

