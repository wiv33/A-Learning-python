r = open("../txt", 'r')
words = []
for read in r.readlines():
    for word in read.split(" "):
        if word == '':
            continue

        word = word.replace(",", "").replace("\n", "")
        words.append(word)

# print(words)

myDictionary = {}

for w in words:

    if w in myDictionary:
        myDictionary[w] = myDictionary[w] + 1
    else:
        myDictionary[w] = 1

print(myDictionary)
