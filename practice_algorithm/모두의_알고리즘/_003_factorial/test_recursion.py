from unittest import TestCase

from .recursion import recursion_sum, recursion_max_val


class Test(TestCase):
    def test_recursion_sum(self):
        self.assertEqual(55, recursion_sum(10))


class TestMaxVal(TestCase):
    def test_recursion_max_val(self):
        self.assertEqual(10, recursion_max_val([2, 3, 4, 9, 10, 7, 6, 7]))
        self.assertEqual(9, recursion_max_val([2, 3, 4, 9, 1, 7, 6, 7]))

