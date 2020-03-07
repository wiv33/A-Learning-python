from rx import from_

"""
This method will convert the given array or object into an observable.
Parameter
    iterator: This is an object or array.
Return value
    This will return an observable for the given iterator.
"""

my_from = from_(range(1, 11))

my_from.subscribe(
    lambda x: print("value is {}".format(x)),
    lambda e: print("Error : {}".format(e)),
    lambda: print("Complete")
)

#result
# value is 1
# value is 2
# value is 3
# value is 4
# value is 5
# value is 6
# value is 7
# value is 8
# value is 9
# value is 10
# Complete