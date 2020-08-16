import re


class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi_loop(self) -> int:
        s = self.data.lstrip()

        if not s:
            return 0

        data = s.split()[0].lstrip()

        length = len(data)
        if (length <= 1 and not data.isdigit()) or self.return_zero(data):
            return 0

        acc = [data[0]]
        is_calculate = re.search(r'^[-+]', acc[0])
        remove_zero = True
        for x in range(1, length):
            # end
            if re.search(r'[a-zA-Z.]', data[x]) or (acc[0] == "0" and not data[x].isdigit()):
                break

            # continue
            if is_calculate and len(acc) < 2 and data[x] == "0":
                continue

            if acc[0] == "0" and remove_zero and data[x] == "0":
                continue

            acc.append(data[x])
            remove_zero = False

        if acc[0] == "0" or (re.search(r'^[-+]', acc[0]) and len(acc) < 2):
            acc.pop(0)

        result = eval(''.join(acc or "0"))
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
