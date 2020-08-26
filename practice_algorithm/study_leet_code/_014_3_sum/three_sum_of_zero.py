# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        idx = 0
        left_idx = idx + 1
        right_idx = len(nums) - 1

        while idx < (len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                left_idx = idx + 1
                right_idx = len(nums) - 1
                continue
            tot_sum = nums[idx] + nums[left_idx] + nums[right_idx]
            # print("t {}".format(tot_sum))
            if tot_sum < 0:
                left_idx += 1
            elif tot_sum > 0:
                right_idx -= 1
            else:
                result.append([nums[idx], nums[left_idx], nums[right_idx]])

                while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                    left_idx += 1

                while right_idx > left_idx and nums[right_idx] == nums[right_idx - 1]:
                    right_idx -= 1

                left_idx += 1
                right_idx -= 1

            if idx < len(nums) - 1 and left_idx >= right_idx:
                idx += 1
                left_idx = idx + 1
                right_idx = len(nums) - 1

        print(result)
        return result
