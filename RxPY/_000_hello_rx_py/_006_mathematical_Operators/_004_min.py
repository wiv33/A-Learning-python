"""this operator will give an observable with min value from the source observable

:parameter
    comparer_function: optional param.
    this function is used on source observables to compare values.

:return
    it returns an observable with min value from the source observable.

"""

from rx import of, operators as op

o = of(12, 32, 41, 52, 62, 502, 555)

o.pipe(
    # op.min(lambda t1, t2: t1 - t2), # Min value is 12
    # op.min(lambda t1, t2: t2 - t1) # Min value is 555
    op.min() # Min value is 12
).subscribe(lambda x: print("Min value is {}".format(x)))

