from sys import stdin

cnt = stdin.readline()

for idx in range(int(cnt)):
    n, m = map(int, stdin.readline().split(" "))
    print("Case #{}: {}".format(idx + 1, n + m))
