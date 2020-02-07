# JSON....

nameIs = 'name'
ageIs = 'age'

x = {
    "name": "String name",
    "age": 30
}

# print(x)

# print(x['name'])
# print(x[nameIs])
# print(x[ageIs])


############################################

y = {
    0: "promise",
    ("String", "Tuple"): "Flux",
    "numbers": [2, 7, 3, 1, 5]
}

# print(y)

# print(y["numbers"])

# print("numbers" in y)  # True

# print(y[("String", "Tuple")])

#########################################

tup1, tup2 = 'empty', "early"
z = {
    0: "promise",
    (tup1, tup2): "Flux",
    "numbers": [2, 7, 3, 1, 5]
}

print(z)

tup1 = 'blank'

# 변화 없음
# print(z)

# error => KeyError: ('blank', 'early')
# print(z[(tup1, tup2)])

# {0: 'promise', ('empty', 'early'): 'Flux', 'numbers': [2, 7, 3, 1, 5], ('blank', 'early'): 'Mono'} # 추가 됨
# z[(tup1, tup2)] = "Mono"

# print(z)
