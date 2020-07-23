import sys

arr: [] = [n for n in range(1000000)]
ps_range: range = range(1000000)

print("expected arr equals ps_range, actual [{}]".format(
    len(arr) == len(ps_range)
))
# expected arr equals ps_range, actual [True]

print(arr == ps_range)
# false

print("arr size : {}\nrange size : {}".format(
    sys.getsizeof(arr), sys.getsizeof(ps_range)
))
# arr size : 8697456
# range size : 48

print(ps_range[77777])
# 77777
