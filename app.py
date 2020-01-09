from math import floor, ceil, sqrt

character_name = "John"
character_age = "31"

isMale = True
print(character_name)
print(character_age)
print(isMale)

print("------------------------------------")
print    ("이것도 허용해줍니다.")

character_name = "Mike"
character_age = 20.52365456345
isMale = False

# upperCase
print(character_name.upper())

# Boolean
print(character_name.upper().isupper())

# Hex
print(character_age.hex())

# length
print(len(character_name))

# String start index -> 0
print(character_name[0])

phrase = "Giraffe Academy"
# like to indexOf
print(phrase.index("i"))
print(phrase.find("A", 0))
print(phrase.replace("Giraffe", "My Body"))


# 연산
print(3 * 4)
print(3 + 4.53)
print(3 * (3 + 2))

print(10 % 3)

myNum = 4

# result 444
print(str(myNum) * 3)

print(str(myNum) + " my favorite number")

# error
# unsupported operand type(s) for +: 'int' and 'str'
# print(myNum + " my favorite number")


myNum = -5
# result : 5
print(abs(myNum))

# -5 ^ 3
print(pow(myNum, 3))

# 7
print(max(4, 7))

print(round(4, 7))

# 3 : 3.0 ~ 3.4
print(round(3.2))

# 4 : 3.5 ~ 3.9
print(round(3.5))

# from math import *
# result : 3 버림
print(floor(3.7))

# 4 올림
print(ceil(3.6))

# 6.0
print(sqrt(36))

