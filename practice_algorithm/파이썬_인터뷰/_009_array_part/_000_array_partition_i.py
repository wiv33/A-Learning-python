# https://leetcode.com/problems/array-partition/
class Solution:
    def __init__(self, data: [int]):
        self.data = data

    def array_pair_sum(self) -> int:
        nums: [int] = self.data
        result = 0
        pair = []
        nums.sort()

        for x in nums:
            pair.append(x)
            if len(pair) == 2:
                print(pair)
                result += min(pair)
                pair = []

        return result

    def array_pair_sum_python(self) -> int:
        return sum(sorted(self.data)[::2])


if __name__ == '__main__':
    print(4 == Solution([1, 4, 3, 2]).array_pair_sum_python())
