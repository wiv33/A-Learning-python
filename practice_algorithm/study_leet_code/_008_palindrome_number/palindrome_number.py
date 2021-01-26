# https://leetcode.com/problems/palindrome-number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        data = str(x)
        start, last = 0, len(data) - 1

        while start <= last:
            if data[start] != data[last]:
                return False
            start += 1
            last -= 1

        return True
