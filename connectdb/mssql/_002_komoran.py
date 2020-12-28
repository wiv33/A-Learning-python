from konlpy.tag import Komoran
import pandas as pd

k = Komoran()

df = pd.read_csv('articles.tsv', sep='\t')

nouns = k.nouns(df.iloc[123860, 0])

words = [word for word in nouns if len(word) > 1]

print(words)

texts = df.iloc[123860, 0].split(' ')
from krwordrank.word import summarize_with_keywords

stopwords = {'기자'}
keywords = summarize_with_keywords(texts, min_count=3, max_length=12,
                                   beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)
print(keywords)
