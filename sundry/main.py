import random

numbers = range(17, 34)

choice = random.choice(numbers)
print(type(choice))
print(choice)

print("#####################")

sample = random.sample(numbers, 3)
print(type(sample))
print(sample)

randint = random.randint(3, 4)
print(type(randint))
print(randint)
