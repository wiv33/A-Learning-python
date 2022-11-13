# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums: [int], target: int) -> [int]:
        # 키와 값을 바꿔서 딕셔너리로 저장
        nums_map = {v: k for k, v in enumerate(nums)}

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return nums.index(n), nums_map[target - n]


if __name__ == '__main__':
    print(Solution().twoSum2([11, 15, 7, 2], 9))
