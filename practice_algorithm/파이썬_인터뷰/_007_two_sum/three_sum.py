# https://leetcode.com/problems/3sum/

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        # n^3 반복
        for i in range(len(nums) - 2):
            # continue duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results

    def three_sum_two_pointer(self, nums: list[int]) -> list[list[int]]:
        # i를 축으로 중복된 값은 건너 뛴다.
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                _sum = sum([nums[i], nums[left], nums[right]])
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 양 옆으로 동일한 값은 스킵한다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results


if __name__ == '__main__':
    print([[-1, -1, 2], [-1, 0, 1]] == Solution().three_sum([-1, 0, 1, 2, -1, -4]))
    print([[-1, -1, 2], [-1, 0, 1]] == Solution().three_sum_two_pointer([-1, 0, 1, 2, -1, -4]))
