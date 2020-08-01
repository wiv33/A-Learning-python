from unittest import TestCase

from euclid import gcd_euclid


class Test(TestCase):
    def test_gcd_euclid(self):
        self.assertEqual(27, gcd_euclid(81, 27))
        self.assertEqual(12, gcd_euclid(60, 24))
        self.assertEqual(1, gcd_euclid(60, 23))
