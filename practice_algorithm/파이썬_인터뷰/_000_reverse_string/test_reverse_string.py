from unittest import TestCase

from .reverse_string import reverse_string


class Test(TestCase):
    def setUp(self):
        self.expected = ['w', 'o', 'l', 'l', 'e', 'h']
        self.actual = ['h', 'e', 'l', 'l', 'o', 'w']

    def test_reverse_string(self):
        reverse_string(self.actual)
        self.assertEqual(self.expected, self.actual)

    def test_reverse_string_be_like_python(self):
        self.actual.reverse()
        self.assertEqual(self.expected, self.actual)