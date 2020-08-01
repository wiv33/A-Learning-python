from unittest import TestCase

from my_gcd import gcd


class Test(TestCase):
    def test_gcd(self):
        self.assertEqual(2, gcd(4, 6))
        self.assertEqual(3, gcd(6, 9))
