"""the operator will group values coming from the source observable based
on the key_mapper function given

:parameter
    key_mapper: this function will take care of

:return
    it returns an observable with values grouped based on the key_mapper function.

"""

from rx import from_, operators as op
import numpy as np

from_(np.array(['A', 'B', 'C', 'D', 'E', 'F']))\
    .pipe(
    op.group_by(lambda v: v[0])
).subscribe(lambda x: print("the element is {}".format(x)))

# result
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BECF08>
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BECFC8>
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BECFC8>
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BF1888>
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BECF88>
# the element is <rx.core.observable.groupedobservable.GroupedObservable object at 0x0000022B34BECE08>