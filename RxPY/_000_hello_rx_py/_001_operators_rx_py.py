import rx
from rx import operators as ops

pipe = rx.range(1, 11) \
    .pipe(ops.filter(lambda i: i % 2 == 0),
          ops.filter(lambda i: i < 3),
          ops.map(lambda i: i + i),
          ops.map(lambda i: i ** i),
          ops.average(lambda x: x + x),
          ops.sum())

pipe.subscribe(lambda x: print("value is {0}".format(x)))
