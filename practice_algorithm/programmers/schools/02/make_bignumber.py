def solution2(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    return ''.join(collected)


if __name__ == '__main__':
    assert "94" == solution2("1924", 2)
