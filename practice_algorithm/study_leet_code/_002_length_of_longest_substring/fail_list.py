class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0

        acc = s[0]
        result = (s[0], len(s[:].split(s[0])))
        # print("{} split is {}".format(s, s[0]))
        if length == result[1] \
                and s[0] == (s[1] or "") \
                and not s[2]:
            return get_answer((s[0], 1))

        for i in range(length - 1):
            l1, l2 = s[i], s[i + 1]
            if l1 == l2:
                acc = s[i + 1]
                continue

            if l1 != l2 and acc[0] != l2:
                acc += l2
                compare_tuple = (acc, len(s[i + 1:].split(acc)))
                # print("tup {}".format(compare_tuple))
                if len(result[0]) < len(compare_tuple[0]):
                    if result[len(result) - 1] == compare_tuple[len(compare_tuple) - 1]:
                        return get_answer((compare_tuple[0], len(compare_tuple[0])))
                    result = compare_tuple

            print(result)
        return get_answer((result[0], len(result[0])))


def get_answer(data: tuple) -> int:
    return data[1]
