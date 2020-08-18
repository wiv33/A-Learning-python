from unittest import TestCase

from ._000_array_partition_i import Solution


class TestSolution(TestCase):
    def test_array_pair_sum(self):
        actual = Solution([1, 4, 2, 3]).array_pair_sum()
        self.assertEqual(4, actual)
