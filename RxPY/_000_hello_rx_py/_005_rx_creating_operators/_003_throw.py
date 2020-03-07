from rx import throw

# This method will create an observable that will throw an error.
my_throw = throw(Exception("There is an Error"))

my_throw.subscribe(
    lambda x: print("value is {}".format(x)),
    lambda e: print("Error : {}".format(e))
)

# result
# Error : There is an Error
