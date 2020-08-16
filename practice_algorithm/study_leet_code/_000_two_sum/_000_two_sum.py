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

    def two_sum(self, nums: [int], target: int) -> [int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    def other_two_sum(self, nums: [int], target: int) -> [int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]


solution = Solution()
two_sum = solution.other_two_sum([1, 5, 7, 8, 9], 10)
print((0, 4) == two_sum)

solution_two_sum = solution.two_sum([1, 5, 7, 8, 9], 10)
print((0, 4) == solution_two_sum)
