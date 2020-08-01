from unittest import TestCase

from fibonacci import fibonacci
from my_gcd import gcd


class Test(TestCase):
    def test_gcd(self):
        self.assertEqual(2, gcd(4, 6))
        self.assertEqual(3, gcd(6, 9))

    def test_fibonacci(self):
        self.assertEqual(21, fibonacci(8, "init"))
