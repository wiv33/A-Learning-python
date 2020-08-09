from unittest import TestCase

from .group_anagrams import Solution


class TestSolution(TestCase):
    def test_group_anagrams(self):
        data = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        actual = Solution(data).group_anagrams()
        expected = {
            'aet': ['eat', 'tea', 'ate'],
            'ant': ['tan', 'nat'],
            'abt': ['bat']
        }
        self.assertIsInstance(expected, dict)
        self.assertIsInstance(actual, dict)
        self.assertDictEqual(expected, actual)
