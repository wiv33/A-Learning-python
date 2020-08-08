import collections


class Solution:
    def __init__(self, data: []):
        self.data = data

    def group_anagrams(self):
        anagrams = collections.defaultdict(list)

        for word in self.data:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams

