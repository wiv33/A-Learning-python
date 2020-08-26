# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        left_idx = 1
        right_idx = len(nums) - 1

        for i in range(len(nums) - 2):
            tot_sum = nums[i] + nums[left_idx] + nums[right_idx]
            if tot_sum == 0:
                print(nums[i], nums[left_idx], nums[right_idx])

            left_idx += 1
            right_idx -= 1
        return result
