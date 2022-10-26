def solution(bell):
    start = {}
    end = {}

    convert_list = [-1 if x == 1 else 1 for x in bell]
    acc = [0] * len(convert_list)
    temp_val = 0
    for x in range(len(convert_list)):
        temp_val += convert_list[x]
        acc[x] = temp_val

    for i, x in enumerate(acc):
        if x not in start:
            start[x] = i
        end[x] = i

    return max(end[x] - start[x] for x in end)


def solution2(bell):
    from itertools import accumulate

    start = {}
    end = {}

    for i, x in enumerate(accumulate([0] + [-1 if b == 1 else 1 for b in bell])):
        if x not in start:
            start[x] = i
        end[x] = i

    return max(end[x] - start[x] for x in end)


if __name__ == '__main__':
    assert 0 == solution([1, 1, 1, 1])
    res = solution([1, 2, 1, 1, 1, 2, 2, 1])
    print('result', res)
    assert 6 == res
