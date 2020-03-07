from datetime import datetime

from rx import timer, operators as op

"""this method will emit the values in sequence after the timout is done.

:parameter
    duetime: time after witch it should emit the first value.
    
:return
    it will return an observable with values emitted after duetime.
"""

timer(5.0, 10).pipe(
    op.map(lambda i: i * i)
).subscribe(lambda x: print("value is {}, current time is {}".format(x, datetime.now().time())))

print("start time is {}".format(datetime.now().time()))
input("press any key to exit\n")

# result
# start time is 19:55:42.269061
# press any key to exit
# value is 0, current time is 19:55:47.278135
# value is 1, current time is 19:55:57.273175
# value is 4, current time is 19:56:07.286588
# value is 9, current time is 19:56:17.273586
# value is 16, current time is 19:56:27.285112