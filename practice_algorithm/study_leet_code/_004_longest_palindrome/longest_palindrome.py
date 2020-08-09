class Solution:
    def __init__(self, data):
        self.data = data
        pass

    def longest_palindrome(self):
        s = self.data
        if len(s) == 0:
            return ""
        if s == s[::-1]:
            return s

        result = ""
        for i in range(0, len(s) - 1):
            acc = s[i]
            for j in range(i + 1, len(s)):
                acc += s[j]

                if len(result) < len(acc) and acc == acc[::-1]:
                    result = acc

        return result
