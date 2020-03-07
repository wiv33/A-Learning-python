"""this operator takes in a function called accumulator function,
that is used on the values coming from the source observable,
and it returns the accumulated values in the form of an observable,
with an optional seed value passed to the accumulator function.

:parameter
    accumulator_func: A function that is used on the values coming from the source observable,
    and it returns the accumulated values in the form of an observable.

    seed: optional. the default value is not set. it is the initial value,
    to be used inside the accumulator function

:return
    it returns an observable, with a single value as output from
    the accumulator function applied on each value of the source observable.
"""

from rx import of, operators as op

of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\
    .pipe(
    op.reduce(lambda acc, x: acc + x)
    # acc: 1, x: 2 -> 3
    # acc: 3, x: 3 -> 6
    # acc: 6, x: 4 -> 10
    # acc: 10, x: 5 -> 15
    # acc: 15, x: 6 -> 21
    # acc: 21, x: 7 -> 28
    # acc: 28, x: 8 -> 36
    # acc: 36, x: 9 -> 45
    # acc: 45, x: 10 -> 55
).subscribe(lambda x: print("value is {}".format(x)))
# result
# value is 55


of("my", "body", "is", "string", "flux")\
    .pipe(
    op.reduce(lambda acc, s: acc + " " + s)
).subscribe(lambda r: print("value is {}".format(r)))
# result
# value is my body is string flux