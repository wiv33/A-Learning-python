"""this operator takes in an observable with values, and converts it into observable
that will have single value. the count function takes in predicate function as an optional argument.
the function is of type boolean, and will add value to the output only, if it satisfies the condition

:parameter
    the count function takes in predicate function as an optional argument.
    the function is of type Boolean, and will add value to the output only, if it satisfies the condition.

:return
    it will return an observable with a single value, i.e. the count from the source observable.

"""

from rx import of, operators as op

test = of(1,2,3,4,5,6,7,8,9,10)

sub1 = test.pipe(
    op.count(lambda x: x % 2)
).subscribe(lambda x: print("the count is {}".format(x)))

# result
# the count is 5

# remove lambda argument the count is 10
