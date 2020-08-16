import re


class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi_loop(self) -> int:
        data = self.data.lstrip()
        if not data or self.return_zero(data):
            return 0




        pass

    def return_zero(self, data):
        search = re.search(r"^[-+[^a-zA-Z]]|^[a-zA-Z]|^[-+]{2}|^[.]", data)
        # print("search is {}".format(search))
        return search
