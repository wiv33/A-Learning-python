# https://leetcode/com/problems/valid-parentheses

# input: ()[]{}
# output: true

# 괄호로 입력된 값이 올바른지 판별

"""
(, [, {는 스택에 푸시
), ], } 스택에서 pop한 결과가 매핑 테이블 결과와 매칭되는지 확인
"""


def is_valid(s):
    stack = []
    # k,v table 생성
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for c in s:
        if c not in table:
            stack.append(c)
        elif not stack or table[c] != stack.pop():
            return False

    # 내용물이 있으면 일치하지 않는다는 의미
    return len(stack) == 0


if __name__ == '__main__':
    assert is_valid("[{}[]()]")
    assert not is_valid("{){}[]")
