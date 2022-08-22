import collections


class Solution:
    def __init__(self, s: str):
        self.s = s
        self.strs = []
        self.strs_deque = collections.deque()

    def calc(self):
        for x in self.s:
            if x.isalnum():
                self.strs.append(x.lower())

        while len(self.strs) > 1:
            if self.strs.pop(0) != self.strs.pop():
                return False

        return True

    def calc2(self):
        for x in self.s:
            if x.isalnum():
                self.strs_deque.append(x.lower())

        while len(self.strs_deque) > 1:
            if self.strs_deque.popleft() != self.strs_deque.pop():
                return False

        return True

    def clac3(self):
        import re
        self.s = self.s.lower()
        self.s = re.sub('[^a-z0-9]', '', self.s)

        return self.s == self.s[::-1]

    def result(self):
        return self.calc() and self.calc2() and self.clac3()
