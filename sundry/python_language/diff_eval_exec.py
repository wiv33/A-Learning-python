code = """for x in range(3):\n\tprint('hello world {}'.format(x)) """
exec(code)
# hello world 0
# hello world 1
# hello world 2


expression = "3 + 7 * a"
a = 12
result = eval(expression)
print(result)
# 87


compile_code = compile('a * b + c', '<string>', 'eval')
print(compile_code)
# <code object <module> at 0x7f6baaf8fea0, file "<string>", line 1>

a, b, c = 3, 7, 12
result2 = eval(compile_code)
print(result2)
# 33

