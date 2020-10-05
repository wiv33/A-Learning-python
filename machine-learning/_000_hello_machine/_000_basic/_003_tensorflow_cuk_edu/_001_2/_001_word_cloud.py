from wordcloud import WordCloud
from collections import Counter
from konlpy import Okt
okt = Okt()
words = ['qwef', 'qbeeb', 'trnrt', 'werw', 'eer', 'qwerhq']
result = dict(Counter(okt.nouns(words)))

wc = WordCloud(
    font_path="font_path",
    width=800,
    height=800,
    background_color='white'
).generate_from_frequencies(result)
