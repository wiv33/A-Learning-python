"""this operator will given an observable with max value from the source observable.

:parameter
    comparer_function: optional param. this function is used on source observables to compare values.

:return
    it returns an observable with max value from the source observable.

"""

from rx import of, operators as op

o = of(12, 24, 50, 33, 72, 80, 520, 1001)
o.pipe(
    # op.max(), # Max value is 1001
    # op.max(lambda t1, t2: t1 - t2), # Max value is 1001
    op.max(lambda t1, t2: t2 - t1) # Max value is 12
    # java compare o1, o2와 같다.
).subscribe(lambda r: print("Max value is {}".format(r)))
