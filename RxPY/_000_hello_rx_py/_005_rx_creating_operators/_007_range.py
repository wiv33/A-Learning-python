from rx import range

"""
this method will give range of integers based on the input given.

:parameters
    start: the first value from which the range will start
    stop: optional, the last value of the range to stop.

:return
    this will return an observable with integer value based on the input given.
"""

my_range = range(0, 10)
my_range.subscribe(
    lambda i: print("value is {}".format(i)),
    lambda e: print("error : {}".format(e)),
    lambda : print("onComplete")
)
# result
# value is 0
# value is 1
# value is 2
# value is 3
# value is 4
# value is 5
# value is 6
# value is 7
# value is 8
# value is 9
# onComplete
#
# Process finished with exit code 0
