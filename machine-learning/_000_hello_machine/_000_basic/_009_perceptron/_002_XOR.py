def XOR():
    F = .0
    T = 1.
    bias = 1.
    return [
               [F, F, bias],
               [F, T, bias],
               [T, F, bias],
               [T, T, bias],
           ], [
               [F],
               [T],
               [T],
               [F]
           ]


x, y = XOR()

print(x, y)
