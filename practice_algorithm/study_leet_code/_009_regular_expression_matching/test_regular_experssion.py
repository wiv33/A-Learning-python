import unittest
from RegularExpression import is_match


class MyTestCase(unittest.TestCase):

    def test_aa_a(self):
        self.assertFalse(is_match('aa', 'a'))

    def test_aa_aAll(self):
        self.assertTrue(is_match('aa', 'a*'))

    def test_ab_dotAll(self):
        self.assertTrue(is_match('ab', '.*'))

    def test_mississippi_false(self):
        self.assertFalse(is_match("mississippi", "mis*is*p*."))


if __name__ == '__main__':
    unittest.main()
