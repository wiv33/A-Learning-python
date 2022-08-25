# https://leetcode.com/problems/reverse-string

class Solution:
    def __init__(self, s: [str]):
        self.strs = s

    def calc(self):
        left, right = 0, len(self.strs) - 1
        while left < right:
            self.strs[left], self.strs[right] = self.strs[right], self.strs[left]
            left += 1
            right -= 1

    def result(self):
        self.calc()
