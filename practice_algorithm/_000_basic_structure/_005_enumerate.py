arr: [] = [1, 2, 3, 4, 5, 23, 7, 8, 3, 5, 6]

print(enumerate(arr))
# <enumerate object at 0x7ffa1c7bfc40>

print(list(enumerate(arr)))

for i, v in enumerate(arr):
    print(i, v)
