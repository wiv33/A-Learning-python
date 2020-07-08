import codecs
from konlpy.tag import Komoran, Twitter

model = Komoran()

line = '나는 국민대학교의 축제에 놀러 가고 싶습니다.'

result = model.pos(line)

print(result)

twitter = Twitter()

print(twitter.pos(line))
