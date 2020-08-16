# https://leetcode.com/problems/string-to-integer-atoi/
import re


def return_zero(data):
    search = re.search(r"[-+[^a-zA-Z]]|[a-zA-Z]|[-+]{2}", data)
    print("search is {}".format(search))
    return search


class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi(self) -> int:
        s = self.data
        not_empty = s.lstrip()
        if not not_empty or not_empty == "+" or not_empty == "-":
            return 0

        data = not_empty.split()[0].lstrip()

        if return_zero(data):
            return 0

        data = re.sub(r'(?<=[-+])0*[^1-9]', "", data)
        print(data)
        data = re.sub(r'0*$[^1-9]', "", data)
        print(data)
        data = re.sub(r'^0*', "", data)
        print(data)
        data = eval(data or "0")

        data = int(data // 1)

        max_num = 2 ** 31
        if -max_num > data:
            return -max_num
        elif max_num - 1 < data:
            return max_num - 1
        else:
            return data
