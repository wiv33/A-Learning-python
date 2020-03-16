"""this operator will collect all the values, from the source observable and emit them at regular intervals once
the given boundary condition is satisfied

:parameter
    boundaries: the input observable that will decide when to stop so that the collected values are emitted

:return
    the return value is observable, that will have all the values collected from source observable based
    and that is time duration is decided by the observable taken.

example)
"""
from rx import of, interval, operators as op
import numpy as np
of(np.arange(1, 10000000)) \
    .pipe(
    op.map(lambda n: (n * (n + 1)) / 2),
    # op.filter(lambda x: x % 3 != 0),
    op.buffer(interval(0.001))
).subscribe(lambda x: print("the element is {}".format(x)))
