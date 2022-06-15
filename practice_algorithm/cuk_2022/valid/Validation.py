def isValid(s):
    bracket_group, stack = {")": "(", "]": "[", "}": "{"}, []
    for c in s:
        if c in '{[(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False

            if bracket_group[c] != stack.pop(find_idx(bracket_group, c, stack)):
                return False

    return len(stack) == 0


def find_idx(bracket_group, c, stack):
    last_index = stack.__len__() - 1
    for j in range(last_index, -1, -1):
        if stack[j] == bracket_group[c]:
            last_index = j
            break
    return last_index


if __name__ == '__main__':
    print(isValid("()") == True)
    print("=" * 33)
    print(isValid("()[]{}") == True)
    print("=" * 33)
    print(isValid("(]") == False)
    print("=" * 33)
    print(isValid("((())") == False)
    print("=" * 33)
    print(isValid("([)]") == True)
    print(isValid("( [ { ) ] }}".replace(" ", '')) == False)
