def length_of_longest_substring(s: str) -> int:
    return get_first_pattern(s)


def get_first_pattern(s: str) -> int:
    length = len(s)

    if length == 0:
        return 0

    acc = s[0] or ""

    if acc * len(s) == s:
        return 1

    if is_high_pass_not_match(s):
        return len(s)

    dictionary = dict()

    for i in range(length - 1):
        l1, l2 = s[i], s[i + 1]

        if acc.__contains__(l2):
            add_dict(dictionary, acc)
            acc = acc[acc.index(l2) + 1:]

        acc += l2

    add_dict(dictionary, acc)
    return result_int(dictionary)


def add_dict(dictionary, acc):
    dictionary.__setitem__(acc, dictionary.get(acc) if acc in dictionary else 1)
    # print(dictionary)


def result_int(dictionary: {}) -> int:
    if len(dictionary) == 1:
        return len(dictionary.popitem()[0])

    max_item = dictionary.popitem()
    for i in sorted(dictionary.items(),
                    key=lambda x: x[1],
                    reverse=True):
        if max_item[1] > i[1]:
            return max_item

        if max_item[1] < i[1]:
            max_item = i
        elif max_item[1] == i[1] and len(max_item[0]) < len(i[0]):
            max_item = i

    return len(max_item[0])


def is_high_pass_not_match(s):
    for z in range(1, len(s)):
        if s[z - 1] == s[z]:
            return False


class Solution:
    pass
