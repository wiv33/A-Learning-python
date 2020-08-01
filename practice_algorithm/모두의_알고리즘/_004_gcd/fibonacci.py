def fibonacci(a, name):
    # a = 7
    # 0 + 1 = 1
    # 1 + 1 = 2
    # 1 + 2 = 3
    # 2 + 3 = 5
    # 3 + 5 = 8
    # 5 + 8 = 13
    # 8 + 13 = 21
    print(f'val:{a}, name:{name}')
    if a < 2:
        print(f'    # finish call: {name} ======')
        return a

    f1 = fibonacci(a - 1, f"first{a - 1}")
    print(f'f1 is "{f1}"', end='\n')
    f2 = fibonacci(a - 2, f"second{a - 2}")
    print(f'f2 is "{f2}"', end='\n')
    print(f'f1[{f1}] + f2[{f2}] : {f1 + f2}')
    return f1 + f2
