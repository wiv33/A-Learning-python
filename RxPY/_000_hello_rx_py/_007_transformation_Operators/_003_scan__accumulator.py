"""this operator will apply an accumulator function to the values coming
from the source observable and return an observable with new values.

:parameter
    accumulator_func: This function is applied to all the values
    from the source observable.

    seed: [optional] The initial value to be used inside in accumulator_func.

:return
    This operator will return an observable that will have new values based
    on the accumulator function applied on each value of the source observable
"""

from rx import of, operators as op

acc_x = lambda acc, x: acc + x
of(1,2,3,4,5,6,7,8,90).pipe(
    op.scan(acc_x, 0)
).subscribe(lambda x: print("this element is {}".format(x)))

# result
# this element is 1
# this element is 3
# this element is 6
# this element is 10
# this element is 15
# this element is 21
# this element is 28
# this
# element is 126