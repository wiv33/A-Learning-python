from rx import start

"""
this method takes in a function as an input, and returns an observable 
that will return value from the input function

:parameter
    func: a function that will be called.
    
:return
    it returns an observable that will have a return value from the input function.
"""
lambdas = [lambda: "Hello RxPy", lambda: 5 * 7]

for item in lambdas:
    my_start = start(item)

    my_start.subscribe(
        lambda x: print("value is {}".format(x)),
        lambda e: print("error {}".format(e)),
        lambda: print("Job Done!")
    )

# result
# value is Hello RxPy
# Job Done!
# value is 35
# Job Done!
