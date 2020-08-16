import re


class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi_loop(self) -> int:
        data = self.data.lstrip()
        if not data or self.return_zero(data):
            return 0

        acc = [data[0]]
        last = 1 if acc[0] in ['-', '+'] else 0
        length = len(data)

        if last == 1 and length == 1:
            return 0

        for x in range(1, length):
            if not data[x].isdigit():
                break

            if len(acc) < last and data[x] == "0":
                continue

            acc.append(data[x])

        join = "".join(acc)
        if (last == 1 and len(join) == 1) or re.search(r'[a-zA-Z]', join):
            return 0

        result = int(join)

        max_result = 2 ** 31
        if result < -max_result:
            return max(-max_result, result)
        elif result > max_result - 1:
            return min(result, max_result - 1)
        return result

    def return_zero(self, data):
        search = re.search(r"^[-+[^a-zA-Z]]|^[a-zA-Z]|^[-+]{2}|^[.]", data)
        # print("search is {}".format(search))
        return search
