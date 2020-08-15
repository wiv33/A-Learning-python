# https://leetcode.com/problems/string-to-integer-atoi/
import re


class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi(self) -> int:
        s = self.data
        not_empty = s.lstrip()
        if not not_empty:
            return 0

        data = not_empty.split()[0].lstrip()

        if data.isalpha():
            return 0

        data = eval(data)

        data = int(data // 1)

        max_num = 2 ** 31
        if -max_num > data:
            return -max_num
        elif max_num - 1 < data:
            return max_num - 1
        else:
            return data
