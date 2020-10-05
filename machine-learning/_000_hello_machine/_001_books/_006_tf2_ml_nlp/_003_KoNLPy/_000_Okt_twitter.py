from konlpy.tag import Okt

okt = Okt()

txt = '한글 자연어 처리는 재밌다 이제부터 열심히 해야지...ㅋㅋㅋㅋㅋ'

print(okt.morphs(txt))
# ['한글', '자연어', '처리', '는', '재밌다', '이제', '부터', '열심히', '해야지', '...', 'ㅋㅋㅋㅋㅋ']
#
print(okt.morphs(txt, norm=True))
# ['한글', '자연어', '처리', '는', '재밌다', '이제', '부터', '열심히', '해야지', '...', 'ㅋㅋㅋ']
#
print(okt.morphs(txt, stem=True))
# ['한글', '자연어', '처리', '는', '재밌다', '이제', '부터', '열심히', '하다', '...', 'ㅋㅋㅋㅋㅋ']
#


"""
명사와 어절 추출하기
"""

# 명사 나운
print(okt.nouns(txt))
# ['한글', '자연어', '처리', '이제']
#

# 어절 프레이즈
print(okt.phrases(txt))
# ['한글', '한글 자연어', '한글 자연어 처리', '이제', '자연어', '처리']
#

"""
품사 태깅
pos
"""

print(okt.pos(txt))
# [('한글', 'Noun'), ('자연어', 'Noun'), ('처리', 'Noun'), ('는', 'Josa'), ('재밌다', 'Adjective'), ('이제', 'Noun'), ('부터',
# 'Josa'), ('열심히', 'Adverb'), ('해야지', 'Verb'), ('...', 'Punctuation'), ('ㅋㅋㅋㅋㅋ', 'KoreanParticle')]
#
print(okt.pos(txt, join=True))
# ['한글/Noun', '자연어/Noun', '처리/Noun', '는/Josa', '재밌다/Adjective', '이제/Noun', '부터/Josa', '열심히/Adverb', '해야지/Verb', '.../Punctuation', 'ㅋㅋㅋㅋㅋ/KoreanParticle']
