def print_args(farg, *args):
    print("formal arg: %s" % farg)
    for arg in args:
        print("another positional arg: %s" % arg)


print_args(1, "two", 3, True, "what", 7, 8, [], {}, str(("a", "b")))
