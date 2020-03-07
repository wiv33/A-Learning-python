from rx import of, operators as op

"""this operator will take in two or more observables and 
give a single observable with all the values in the sequence.

:parameter
    Observables: list of observables to be concatenated.
    
:return
    An observable is returned with a single value merged from the values of the source observable.
    
"""

my_ob_1 = of(2,4,6,8,10,12)
my_ob_2 = of(3,6,9,12,15)
my_ob_3 = of("my","body","is")

my_ob_1.pipe(
    op.concat(my_ob_2),
    op.concat(my_ob_3)
).subscribe(lambda x: print("final value is {}".format(x)))

# result
# final value is 2
# final value is 4
# final value is 6
# final value is 8
# final value is 10
# final value is 12
# final value is 3
# final value is 6
# final value is 9
# final value is 12
# final value is 15
# final value is my
# final value is body
# final value is is
#
# Process finished with exit code 0
