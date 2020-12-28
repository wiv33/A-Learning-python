import konlpy
from konlpy.tag import Okt
import pandas as pd

o = Okt()
df = pd.read_csv('articles.tsv', sep='\t')
print(df.iloc[123860, 0])

print(o.morphs(df.iloc[123860, 0]))

noun_list = [s[0] for s in o.pos(df.iloc[123860, 0]) if s[1] == 'Noun' and len(s[0]) > 1]
temp_list = o.pos(df.iloc[123860, 0])

print(noun_list, len(temp_list))

from krwordrank.sentence import summarize_with_sentences

penalty = lambda x: 0 if (25 <= len(x) <= 80) else 1

stopwords = {'기자'}

keywords, sents = summarize_with_sentences(
    o.morphs(df.iloc[123860, 0]),
    penalty=penalty,
    stopwords=stopwords,
    diversity=0.7,
    num_keywords=100,
    num_keysents=10,
    scaling=lambda x: 1,
    verbose=False,
)

# print(keywords)
print(sents)
