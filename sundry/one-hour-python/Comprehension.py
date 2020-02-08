numbers = range(10)

odd_numbers = []

for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)

###

odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)