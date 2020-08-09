from unittest import TestCase

from .find_median_sorted_array import Solution


class TestSolution(TestCase):
    def test_find_median_sorted_arrays(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        result = Solution(nums1, nums2)\
            .find_median_sorted_arrays()

        self.assertEqual(2.5, result)
