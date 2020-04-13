"""this operator will change each value from the source observable into
a new value based one the output of the mapper_func given

:parameter
    mapper_func: (optional) It will change the values from the source observable based
    one the output coming from this function.

"""

from rx import from_, of, operators as op
import numpy as np


def myOfTest(arr: object) -> None:
    of(arr).pipe(op.map(lambda n: n * n)).subscribe(
        lambda x: print("this object is {}".format(x)))


def myFromTest(arr: object) -> None:
    from_(arr).pipe(
        # op.filter(lambda n: n % 2 == 0),
        op.map(lambda n: n *n)
    ).subscribe(
        lambda x: print("this element is {}".format(x)))

myOfTest(np.array(range(1, 11)))
# result
# this object is [  1   4   9  16  25  36  49  64  81 100]

myFromTest([1, 2, 3, 4, 5, 6, 7, 8, 90])
# result
# this element is 1
# this element is 4
# this element is 9
# this element is 16
# this element is 25
# this element is 36
# this element is 49
# this element is 64
# this element is 8100