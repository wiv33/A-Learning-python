from rx import of, operators as op

"""this operator will calculate the average from 
the source observable given and output an observable that will have the average value.


"""
my_of = of(1,2,3,4,5,6,7,8,9,10)

my_of.pipe(
    op.average()
).subscribe(lambda i: print("average is {}".format(i)))

# result
# value is 5.5