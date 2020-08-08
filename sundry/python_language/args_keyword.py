def print_args(farg, *args):
    print("formal arg: %s" % farg)
    for arg in args:
        print("another positional arg: %s" % arg)


print_args(1, "two", 3, True, "what", 7, 8, [], {}, str(("a", "b")))
# formal arg: 1
# another positional arg: two
# another positional arg: 3
# another positional arg: True
# another positional arg: what
# another positional arg: 7
# another positional arg: 8
# another positional arg: []
# another positional arg: {}
# another positional arg: ('a,', 'b')