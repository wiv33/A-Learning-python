from _001_comprehension_arr import contain_j, contain_e

# java의 iterator
generator_tuple_j_e = ((j, e) for j in contain_j for e in contain_e)
print(type(generator_tuple_j_e))
# <class 'generator'>

print(next(generator_tuple_j_e))
# ('java', 'elasticsearch')
print("--- split ---")
for gen in generator_tuple_j_e:
    print(gen)
    # ('java', 'reactive')
#     남아있는 한 개의 튜플만 출력

print("next part", end=" \n")


def ps_gen():
    yield 'ps'
    yield 1
    yield [1, 2, 3, 4, 5]
    yield True


gen_next = ps_gen().__next__()
print(gen_next)


# ps
def print_gen(generator):
    g = generator
    print(g.__hash__())
    for gen in g:
        print("v => {}".format(gen), end='\n')


print_gen(ps_gen())

print("--- split ---")

g = ps_gen()
print(next(g))
print_gen(g)

""" 

ps
8740000442042
v => ps
v => 1
v => [1, 2, 3, 4, 5]
v => True
--- split ---
ps
8740000442042
v => 1
v => [1, 2, 3, 4, 5]
v => True
"""
