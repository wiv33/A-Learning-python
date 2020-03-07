from rx import just

"""
:parameter
    value: to be converted to an observable
    
:return
    it will return an observable with the given values
"""

my_just = just((10, 52, 34, 55, 81))

my_just.subscribe(
    lambda x: print("value is {}".format(x)),
    lambda e: print("error : {}".format(e)),
    lambda : print("complete")
)
# result
# value is (10, 52, 34, 55, 81)
# complete

my_just_dict = just(dict({"Key": "my Body", "value": "is"}))

my_just_dict.subscribe(
    lambda x: print("value is {}".format(x)),
    lambda e: print("error : {}".format(e)),
    lambda : print("complete")
)
# result
# value is {'Key': 'my Body', 'value': 'is'}
# complete