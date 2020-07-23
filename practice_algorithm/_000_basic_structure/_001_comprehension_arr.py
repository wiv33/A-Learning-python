arr: [] = ['sori', 'elasticsearch', 'python', 'java', 'spring', 'reactive', 'rx']

contain_j = [x for x in arr if x.__contains__("j")]
print(contain_j)
# ['java']

contain_e = [x for x in arr if x.__contains__("e")]
print(contain_e)
# ['elasticsearch', 'reactive']

list_tuple_j_e = [(j, e) for j in contain_j for e in contain_e]
print(list_tuple_j_e)
# [('java', 'elasticsearch'), ('java', 'reactive')]

print("[{}] > [{}]".format(type(list_tuple_j_e), type(list_tuple_j_e[0])))
# [<class 'list'>] > [<class 'tuple'>]

