from werkzeug.datastructures import MultiDict

# Key, String
post = MultiDict()
post.add("key", "value")


# key, list
listDict = MultiDict()
listDict.add("key", ["v1", "v2"])

# default
defaultDict = MultiDict()
defaultDict.add("foo", "s")
defaultDict.setdefault("foo", "my")
defaultDict.setdefault("lorem", "body")

# result: MultiDict([('foo', 's'), ('lorem', 'body')])
"""actually
    if key not in self:
        self[key] = default
    else:
        default = self[key]
    return default
"""
# print(defaultDict)


post.clear()
# listDict.clear()
defaultDict.clear()

# deep copy

# 원본
# MultiDict([('key', ['v1', 'v2'])])
# print(listDict)

list_copy = listDict.copy()
list_deep_copy = listDict.deepcopy()

deep = list_deep_copy["key"].extend(["ham3"])
# MultiDict([('key', ['v1', 'v2'])])
# print(listDict)

copy = list_copy["key"].extend(["ham3"])
# MultiDict([('key', ['v1', 'v2', 'ham3'])])
# print(listDict)

listDict.clear()


# POP
pop = MultiDict()
pop.add("foo", "bar")

foo_value = pop.pop("foo")
# print("foo" in pop) # false


# list
pop_list = MultiDict()
pop_list.add("foo", ["foo", "bar", "name"])


pop_list_values = pop_list.pop("foo")
# ['foo', 'bar', 'name']

# pop_list_values = pop_list.poplist("foo")
# [['foo', 'bar', 'name']]


# update
# - 기존 MultiDict 에 다른 MultiDict 내용을 삽입할 때 사용

md = MultiDict()
md.add("foo", "bar")

md2 = MultiDict()
md2.add("lorem", "large")

md.update(md2)
# MultiDict([('foo', 'bar'), ('lorem', 'large')])

# 병합 이후 데이터 존재 확인
# print(md2)
# MultiDict([('lorem', 'large')])

