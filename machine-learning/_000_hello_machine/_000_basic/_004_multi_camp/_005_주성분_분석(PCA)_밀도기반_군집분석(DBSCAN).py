from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pandas as pd
import numpy as np
import rx
from rx import operators as ops
import matplotlib.pyplot as plt

# rx.of(pd.read_csv('wholesale.csv')) \
#     .subscribe(lambda x: print("{}".format(x)))

"""
패턴만 분석하는 비지도학습
"""

# sale 데이터 호출
data = pd.read_csv('wholesale.csv')
# print(data.shape)

print(data.head())

# 차원 축소
pca = PCA(n_components=2)

result = pca.fit_transform(data)

stscaler = StandardScaler().fit(result)
res = stscaler.transform(result)
print(res)

plt.scatter(res[:, 0], res[:, 1], s=2, c='blue')
plt.xlabel("pca-1")
plt.ylabel("pca-2")
plt.title('Wholesale Data - PCA')
plt.savefig('pca_wholesale.png', format='png')

# 밀도기반 군집분석 (DBSCAN)

# min_samples: 어느정도의 밀집도를 가져야 core로 인정해주는지 값을 설정
dbsc = DBSCAN(eps=.5, min_samples=15).fit(res)
labels = dbsc.labels_

core_samples = np.zeros_like(labels, dtype=bool)
core_samples[dbsc.core_sample_indices_] = True

print(core_samples, core_samples.shape)

# 시각화
unique_labels = np.unique(labels)
print(unique_labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
print(colors)

# 군집과 노이즈를 색상으로 구분
for (label, color) in zip(unique_labels, colors):
    class_member_mask = (labels == label)
    xy = res[class_member_mask & core_samples]
    plt.scatter(xy[:, 0], xy[:, 1], c=color, s=2)

    xy2 = res[class_member_mask & ~core_samples]
    plt.scatter(xy2[:, 0], xy2[:, 1], c=color, s=2)

plt.title('DBSCAN on wholesale data')
plt.xlabel("pca-1")
plt.ylabel("pca-2")
plt.savefig('dbscan_wholesale_pca.png', format='PNG')
