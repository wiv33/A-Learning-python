def solution(bell):
    if not (bell.__contains__(1) and bell.__contains__(2)):
        return 0

    if len(bell) == 2:
        return 2

    number = get_less_then_number(bell, 0, len(bell))

    


    raise Exception()


def get_less_then_number(arr=None, start=0, end=0):
    if arr is None:
        arr = []

    cnt_arr = arr[start:end]
    cnt_one = cnt_arr.count(1)
    cnt_two = cnt_arr.count(2)
    if cnt_one == cnt_two:
        return 0
    elif cnt_two < cnt_one:
        return 2
    else:
        return 1


if __name__ == '__main__':
    assert 0 == solution([1, 1, 1, 1])
    i = solution([1, 2, 1, 1, 1, 2, 2, 1])
    print('result', i)
    assert 6 == i
