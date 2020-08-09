# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def find_median_sorted_arrays(self) -> float:
        s = sorted(self.nums1 + self.nums2)
        divide, mod = divmod(len(s), 2)
        return sum([s[divide - 1], s[divide]]) / 2 if mod % 2 == 0 else s[divide]
