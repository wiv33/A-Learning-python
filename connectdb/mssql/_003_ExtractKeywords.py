from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from konlpy.tag import Okt

vectorizer = TfidfVectorizer(min_df=.0,
                             analyzer='word',
                             sublinear_tf=True,
                             ngram_range=(1, 3),
                             max_features=6000)
"""
min_df: 
    설정한 값보다 특정 토큰의 df 값이 더 적게 나오면 벡터화 과정에서 제거
    
analyzer: 
    분석하기 위한 기준 단위
        word - 단어
        char - 하나의 문자
        
sublinear_tf:
     문서의 빈도 수에 대한 스무딩 여부 결정
     smoothing
     
ngram_range:
    빈도의 기본 단위 범위
    
max_features:
    각 벡터의 최대 길이
    특징의 길이를 설정
    
"""


def get_ranks(directed_graph_weights, d=0.85):
    A = directed_graph_weights
    matrix_size = A.shape[0]
    for _id in range(matrix_size):
        A[_id, _id] = 0
        col_sum = np.sum(A[:, _id])
        if col_sum != 0:
            A[:, _id] /= col_sum
        A[:, _id] *= -d
        A[_id, _id] = 1

    B = (1 - d) * np.ones((matrix_size, 1))

    ranks = np.linalg.solve(A, B)
    return {idx: r[0] for idx, r in enumerate(ranks)}


def get_word(idf, value_num):
    return [k for k, v in idf.vocabulary_.items() if v in value_num]


def distinct_sentences(sentences):
    result_list = []
    for s in sentences:
        ret_sent = set()
        for word in s.split():
            ret_sent.add(word)
        result_list.append(' '.join(ret_sent))
    return np.array(result_list)


def refine_sentences(ss):
    o = Okt()
    ret = []
    for s in ss:
        words = [tagging[0] for tagging in o.pos(s) if
                 len(tagging[0]) > 1 and (
                         tagging[1] == 'Noun' or tagging[1] == 'Adjectives' or tagging[1] == 'Pronouns')]
        ret.append(' '.join(words))

    # print('ret is :')
    # print(ret)
    return ret


df = pd.read_csv('articles.tsv', sep='\t')
# sentences = distinct_sentences(df.iloc[-10000:, 0].dropna(axis=0).values)
sentences = refine_sentences(df.iloc[-20000:, 0].dropna(axis=0).values)
print(f'ret size : {len(sentences)}')
# reviews: [sentence, sentence, sentence]
vectorizer.fit(sentences)


def get_keywords(target_vectorizer, iterable_sentence_one):
    tfidf = target_vectorizer.transform(iterable_sentence_one).toarray()
    sent_graph = np.dot(tfidf, tfidf.T)
    ranks = get_ranks(sent_graph, d=0.33)
    result = sorted(ranks, key=lambda x: ranks[x], reverse=True)

    print(iterable_sentence_one)
    print(ranks)
    print(result)

    return get_word(target_vectorizer, result)


print(get_keywords(vectorizer, sentences[300:305]))
