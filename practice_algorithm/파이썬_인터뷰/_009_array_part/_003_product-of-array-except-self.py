# https://leetcode.com/problems/product-of-array-except-self/

#  input: [1,2,3,4]
#  output [24,12,8,6]

# required: 나눗셈을 하지 않고 O(n)에 풀이

def product_except_self(nums: [int]) -> [int]:
    out = []
    p = 1

    # 왼쪽 곱
    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p *= nums[i]

    return out


print([24, 12, 8, 6] == product_except_self([1, 2, 3, 4]))
