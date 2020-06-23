from sys import stdin

cnt = int(stdin.readline())

for x in range(cnt - 1):
    print("{}{}".format(" " * (cnt - 1 - x), "*" * (x + 1)))

print("*" * cnt)
