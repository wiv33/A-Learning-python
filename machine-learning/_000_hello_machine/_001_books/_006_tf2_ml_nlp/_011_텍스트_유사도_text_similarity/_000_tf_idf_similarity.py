from sklearn.feature_extraction.text import TfidfVectorizer

sent = ('휴일 인 오늘 도 서쪽 을 중심 으로 폭염 이 이어졌는데요, 내일 은 반가운 비 소식 이 있습니다.',
        '폭염 을 피해서 휴일 에 놀러왔다가 갑작스런 비 로 인해 망연자실 하고 있습니다.',)

tfidf = TfidfVectorizer()

tfidf_metrics = tfidf.fit_transform(sent)
idf = tfidf.idf_
print(dict(zip(tfidf.get_feature_names(), idf)))
# {'갑작스런': 1.4054651081081644, '내일': 1.4054651081081644, '놀러왔다가': 1.4054651081081644, '망연자실': 1.4054651081081644, '반가운': 1.4054651081081644, '서쪽': 1.4054651081081644, '소식': 1.4054651081081644, '오늘': 1.4054651081081644, '으로': 1.4054651081081644, '이어졌는데요': 1.4054651081081644, '인해': 1.4054651081081644, '있습니다': 1.0, '중심': 1.4054651081081644, '폭염': 1.0, '피해서': 1.4054651081081644, '하고': 1.4054651081081644, '휴일': 1.0}


"""cosine"""

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(tfidf_metrics[0:1], tfidf_metrics[1: 2]))
# [[0.17952266]]

""" euclidean distance or L2 distance1"""

from sklearn.metrics.pairwise import euclidean_distances
import numpy as np


def l1_normalize(v):
    return v / np.sum(v)


print(euclidean_distances(tfidf_metrics[:1], tfidf_metrics[1:]))
# [[1.28099753]]
print(l1_normalize(tfidf_metrics))
#   (0, 11)	0.03689012230748532
#               ...
#   (1, 14)	0.058337445910456025
#   (1, 11)	0.04150757323956731
#   (1, 13)	0.04150757323956731
#   (1, 16)	0.04150757323956731

normalize = l1_normalize(tfidf_metrics)
print(euclidean_distances(normalize[:1], normalize[1:]))
# [[0.20491229]]

from sklearn.metrics.pairwise import manhattan_distances

print(manhattan_distances(tfidf_metrics[:1], tfidf_metrics[1:]))
# [[4.86774417]]

print(manhattan_distances(normalize[:1], normalize[1:]))
# [[0.77865927]]
