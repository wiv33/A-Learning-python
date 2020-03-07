from rx import repeat_value

"""
this method will create an observable that will repeat the given value as per the count is given

:parameter
    value: optional. the value to be repeated
    repeat_count: optional. the number of times the given value to be repeated.

:return
    it will return an observable the will repeat the given value as per the count is given.
"""

my_repeat = repeat_value(77, 10)

my_repeat.subscribe(
    lambda x: print("value is {}".format(x)),
    lambda e: print("error : {}".format(e)),
    lambda : print("Complete")
)

# result
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# value is 77
# Complete
