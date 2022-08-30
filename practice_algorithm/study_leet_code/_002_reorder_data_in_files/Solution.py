# https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def __init__(self, s: [str]):
        self.logs = s
        self.digits = []
        self.letters = []

    def calc(self):
        self.appender()
        self.sorted()
        return self.merge()

    def appender(self):
        for log in self.logs:
            if log.split()[1].isdigit():
                self.digits.append(log)
            else:
                self.letters.append(log)

    def sorted(self):
        self.letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    def merge(self):
        return self.letters + self.digits

    def result(self):
        return self.calc()
