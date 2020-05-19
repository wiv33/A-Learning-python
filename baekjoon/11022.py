from sys import stdin

cnt = int(stdin.readline())

for x in range(cnt):
    n, m = map(int, stdin.readline().split(" "))
    print("Case #{}: {} + {} = {}".format(x + 1, n, m, n + m))
