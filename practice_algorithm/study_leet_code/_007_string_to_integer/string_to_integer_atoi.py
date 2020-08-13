# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi(self) -> int:
        s = self.data
        data = s.lstrip().split()[0]

        is_float = data.split(".")[0]
        is_negative = data.startswith("-")

        if is_float.isdigit():
            return int(is_float)

        if is_negative and data[1:].isdigit():
            return -int(data[1:])

        if not data.isdigit():
            return 0

        data = int(data)

        max_num = 2 ** 31
        if -max_num > data:
            return -max_num
        elif max_num - 1 < data:
            return max_num - 1
        else:
            return data
