from rx import interval, operators as ops

"""
this method will give a series of values produced after a timeout.

:parameter
    period: to start the Number sequence
    
:return value
    it returns an observable with all the values in sequential order
"""

my_interval = interval(1.2).pipe(
    ops.map(lambda i: i * i),
    # ops.map(lambda x: x + " x") ## TypeError: unsupported operand type(s) for +: 'int' and 'str'
).subscribe(lambda x: print("value is {}".format(x)))

input("press any key to exit\n")
