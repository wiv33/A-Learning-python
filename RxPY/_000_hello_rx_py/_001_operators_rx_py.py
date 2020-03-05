import rx
from rx import operators as ops

pipe = rx.range(1, 11).pipe(ops.filter(lambda i: i % 2 == 0), ops.sum())

pipe.subscribe(lambda x: print("value is {0}".format(x)))
