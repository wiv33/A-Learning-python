from konlpy.corpus import kobill
from konlpy.tag import Okt

read = kobill.open('1809890.txt').read()
print(read)

okt = Okt()

print(okt.pos(read, stem=True, join=True))

print(okt.nouns(read))
print(okt.phrases(read))
