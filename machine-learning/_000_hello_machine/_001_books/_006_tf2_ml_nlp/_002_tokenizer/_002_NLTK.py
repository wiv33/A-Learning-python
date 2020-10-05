# import nltk
# nltk.download()
from nltk import word_tokenize

"""
영어 토크나이징 라이브러리
Natural Language Toolkit
"""

sentence = "Natural language processing (NLP) is a subfield of computer science, information engineering, " \
           "and artificial intelligence concerned with the interactions between computers and human (natural) " \
           "languages, in particular how to program computers to process and analyze large amounts of natural " \
           "language data."
print(word_tokenize(sentence))
# ['Natural', 'language', 'processing', '(', 'NLP', ')', 'is', 'a', 'subfield', 'of', 'computer', 'science', ',',
# 'information', 'engineering', ',', 'and', 'artificial', 'intelligence', 'concerned', 'with', 'the', 'interactions',
# 'between', 'computers', 'and', 'human', '(', 'natural', ')', 'languages', ',', 'in', 'particular', 'how', 'to',
# 'program', 'computers', 'to', 'process', 'and', 'analyze', 'large', 'amounts', 'of', 'natural', 'language', 'data',
# '.']
