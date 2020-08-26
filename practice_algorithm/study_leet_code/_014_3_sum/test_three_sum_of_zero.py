from unittest import TestCase

from .three_sum_of_zero import Solution


class TestSolution(TestCase):
    def test_three_sum(self):
        actual = Solution().threeSum([-1, 0, 1, 2, -1, -4])
        self.assertListEqual([
            [-1, 0, 1],
            [-1, -1, 2]
        ], actual)

    def test_three_sum_(self):
        actual = Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
        self.assertListEqual(
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
            , actual)
