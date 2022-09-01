class Solution:
    def __init__(self, s: str, banned: [str]):
        self.s = s
        self.banned = banned

    def search(self):
        import collections
        return collections.Counter([word for word in self.preprocessing() if word not in self.banned]).most_common(
            1).pop()[0]

    def preprocessing(self):
        import re
        return re.sub('[^\\w]', ' ', self.s).lower().split()

    def result(self):
        return self.search()
