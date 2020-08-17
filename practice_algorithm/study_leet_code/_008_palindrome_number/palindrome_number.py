# https://leetcode.com/problems/palindrome-number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return False

        max_val = 10
        while x // max_val != 0:
            max_val *= 10

        loop = 1
        # max_val //= 10
        while max_val >= loop:
            f, s = x // max_val, x // loop
            print(f, s)
            # print(max_val, loop, end='\n')
            max_val //= 10
            loop *= 10
        return True
