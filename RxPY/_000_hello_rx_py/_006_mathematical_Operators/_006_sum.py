"""this operator will return an observable with the sum of all the values from source observables.

:parameter
    key_mapper: optional. this is the function,
    that is applied to the values coming from the source observable.

:return
    it returns an observable with the sum of all the values from the source observable.

"""

from rx import of, operators as op

of(1,2,3,4,5,6,7,8,9,10)\
    .pipe(
    # op.sum() # the sum is 55
    op.sum(lambda n: n + 1) # the sum is 65
).subscribe(lambda x: print("the sum is {}".format(x)))
