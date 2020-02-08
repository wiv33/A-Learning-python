num = input('계산할 숫자 입력 : ')
print(num)

i = int(num)
for n in range(i, i + 1):
    for y in range(1, 10):
        print('{}*{} = {}'.format(n, y, n * y))

