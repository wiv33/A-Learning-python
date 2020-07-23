data = {
    "ps": "awesome",
    "flux": "mono"
}
a: {} = {}

for k, v in data.items():
    a[k] = v

print("a => {}".format(a))
# a => {'ps': 'awesome', 'flux': 'mono'}

a = {
    "number": "is"
}

a = {k: v for k, v in data.items()}
print("next a => {}".format(a))
# next a => {'ps': 'awesome', 'flux': 'mono'}
