from rx import never

# It will return an observable that will never complete.
my_never = never()

my_never.subscribe(
    lambda x: print("The value id {}".format(x)),
    lambda e: print("Error : {}".format(e)),
    lambda: print("Complete")
)

#result
# [empty]