import pprint


def my_func():
    pass


def my_not_empty():
    a: {} = {}
    b: [] = []
    c: () = ()
    a['name'] = "ps"


x = 'x'
y = 'thumb'

pprint.pprint(locals())
"""
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': '/home/ps/dev/python/PycharmProjects/learning-python/practice_algorithm/_000_basic_structure/_007_locals.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f3901338c10>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'my_func': <function my_func at 0x7f38e3994c10>,
 'my_not_empty': <function my_not_empty at 0x7f38e3994b80>,
 'pprint': <module 'pprint' from '/usr/lib/python3.8/pprint.py'>,
 'x': 'x',
 'y': 'thumb'}
"""