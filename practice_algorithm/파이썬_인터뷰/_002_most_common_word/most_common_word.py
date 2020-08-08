import collections
import re


class Solution:
    def __init__(self, input_data, banned):
        self.data = input_data
        self.banned = banned

    def most_common_word(self):
        words = [word for word in re.sub(r'[^\w]', ' ', self.data).lower().split() if word not in self.banned]
        counts = collections.Counter(words)
        for word in words:
            counts[word] += 1

        common = counts.most_common(1)
        # print(common)
        # [('ball', 4)]
        assert type(common) == list
        assert type(common[0]) == tuple
        assert type(common[0][0]) == str

        return common[0][0]
