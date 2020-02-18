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
listDict.clear()
defaultDict.clear()