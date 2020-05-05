a = 472
b = 385


def getNum(n, digit):
    digit_num = pow(10, digit)
    div, mod = divmod(n, digit_num)
    return div % 10


assert getNum(a, 2) == 4
assert getNum(a, 1) == 7
assert getNum(a, 0) == 2


