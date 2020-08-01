class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # return [(i, j) for i, v in enumerate(nums) for j, k in enumerate(nums) if
        #         i != j and nums[i] + nums[j] == target][0]

        for i, v in enumerate(nums):
            for j, k in enumerate(nums):
                if i == j:
                    break

                if target == nums[i] + nums[j]:
                    return [i, j]
