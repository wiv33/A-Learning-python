from unittest import TestCase

from .three_sum_of_zero import Solution


class TestSolution(TestCase):
    def test_three_sum(self):
        actual = Solution().threeSum([-1, 0, 1, 2, -1, -4])
        self.assertListEqual([
            [-1, 0, 1],
            [-1, -1, 2]
        ], actual)
