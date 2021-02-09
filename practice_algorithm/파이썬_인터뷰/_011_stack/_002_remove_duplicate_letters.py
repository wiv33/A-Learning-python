# https://leetcode.com/problems/remove-duplicate-letters/

# input: bcabc
# output: abc

# 중복된 문자를 제외하고 사전식 순서로 나열

def remove_duplicate_letters(s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + remove_duplicate_letters(suffix.replace(char, ''))

    return ''


# 스택을 이용한 문자 제거
# stack.append
# seen.add

import collections

def remove_duplicate_letters(s: str) -> str:
    counter, stack = collections.Counter(s), []

    for char in s:
        counter[char] -= 1
        if char in stack:
            continue

        #         뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)

    return ''.join(stack)


if __name__ == '__main__':
    assert "abc" == remove_duplicate_letters("bcabc")
    assert "acdb" == remove_duplicate_letters("cbacdcbc")

