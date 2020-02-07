# Tuple은 list와 동일하지만 불변하다. final스럽다
# mutable  vs  immutable
tpl = tuple()

x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "world")

# print(tpl)  # ()
# print(x + y)
# print(y)
# print(z)

print(sum(x))

# error
# print(sum(y))

