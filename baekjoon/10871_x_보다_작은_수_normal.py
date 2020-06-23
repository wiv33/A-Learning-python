from sys import stdin

cnt, x = map(int, stdin.readline().split(" "))
arr = [n for n in stdin.readline().strip().split(" ") if x > int(n)]
print(' '.join(arr))




