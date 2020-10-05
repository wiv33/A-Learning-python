from konlpy.corpus import kolaw
from konlpy.tag import Okt

read_ = kolaw.open('constitution.txt').read()  # [:20]
print(read_)

okt = Okt()

# 형태소 단위로 나눈다.
print(okt.morphs(read_, stem=True))
