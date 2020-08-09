# import collections
class SolutionOther:
    def sol(self, s: str) -> str:
        if not s:
            return ""

        if s == s[::-1]:
            return s

        result = ""
        for i in range(len(s)):
            temp = self.newfun(s, i, i)
            print("first: {}".format(temp))

            if len(temp) > len(result):
                result = temp

            temp = self.newfun(s, i, i + 1)
            if len(temp) > len(result):
                result = temp

            print("# second: {}".format(temp))
        print("=========================================================================")
        return result

    def newfun(self, s, left, right):
        while 0 <= left and right < len(s) and s[right] == s[left]:
            right += 1
            left -= 1
        return s[left + 1:right]
