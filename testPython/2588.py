a = 472
b = 385


def getNum(n, digit):
    digit_num = pow(10, digit)
    div, mod = divmod(n, digit_num)
    return div % 10


assert getNum(b, 2) == 3
assert getNum(b, 1) == 8
assert getNum(b, 0) == 5

o = getNum(b, 0) * a
t = getNum(b, 1) * a
h = getNum(b, 2) * a
print("%d\n%d\n%d\n%d" % (o, t, h, o + (t * 10) + (h * 100)))
