# https://leetcode.com/problems/longest-palindromic-substring/


def longest_palindrome_substring(s: str) -> str:

    def expend(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     expend(i, i + 1),
                     expend(i, i + 2),
                     key=len)

    return result


if __name__ == '__main__':
    assert "bab" == longest_palindrome_substring("babad")
    assert "bb" == longest_palindrome_substring("cbbd")
    assert "c" == longest_palindrome_substring("c")
