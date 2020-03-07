from rx import empty

my_empty = empty()

my_empty.subscribe(
   on_next=lambda x: print("The value is {0}".format(x)),
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda: print("Job Done!")
)

# result
# Job Done!