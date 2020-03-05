from rx import range, operators as op

test = range(1, 11)

sub1 = test.pipe(
    op.filter(lambda s: s % 2 == 0), # next x -> 2, 4, 6, 8, 10
    op.reduce(lambda acc, x: acc + x, 3)
    # acc: 3, x: 2 -> 5
    # acc: 5, x: 4 -> 9
    # acc: 9, x: 6 -> 15
    # acc: 15, x: 8 -> 23
    # acc: 23, x: 10 -> 33
)

sub1.subscribe(lambda x: print("This value {}".format(x)))