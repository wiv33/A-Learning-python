# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        table = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for x in s:
            if x not in table:
                stack.append(x)
            elif not stack or table[x] != stack.pop():
                return False

        return len(stack) == 0
