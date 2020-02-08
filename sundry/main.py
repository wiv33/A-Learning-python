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

for n in range(20):
    you___format = "this is for you. [{} + {}] ".format(random.sample(range(1, 46), 6), random.choice(range(1, 46)))
    print(you___format)

