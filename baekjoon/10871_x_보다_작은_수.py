from sys import stdin

from rx import from_, operators as op

cnt, x = map(int, stdin.readline().split(" "))

arr = stdin.readline().strip().split(" ")

from_(arr) \
    .pipe(
    op.map(lambda s: int(s)),
    op.filter(lambda n: x > n),
    op.map(lambda t: str(t)),
    op.reduce(lambda acc, s: acc + " " + s)
).subscribe(lambda res: print("{}".format(res)))
