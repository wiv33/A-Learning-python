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

