import pandas as pd
import matplotlib.pyplot as plt
import random
from collections import Counter
from scipy import stats

# 사용자 ID를 키로 갖고 상품 코드의 셋을 값으로 갖는 딕셔너리와
# 상품 코드를 키로 갖고 사용자 ID의 셋을 값으로 갖는 딕셔너리
from sklearn.cluster import KMeans

user_product_dict = {}
product_user_dict = {}

# 상품 코드를 키로 갖고 상품명을 값으로 갖는 딕셔너리
# 군집화의 내용을 확인하는 단계에서 상품명을 사용한다.
product_id_name_dict = {}

excel = pd.read_excel("./_000_Online_Retail.xlsx", header=1)
items = excel.dropna() # row에 NaN column 이 한개 이상 포함되어 있을 경우 제외시킨다.
for i, v in items.iterrows():
    user_code = v.values[6]
    product_id = v.values[1]
    product_name = v.values[2]
    country = v.values[7]

    # 유저 코드가 없거나 영국이 아닐 경우
    if country != 'United Kingdom':
        continue

    invoiceDate = v.values[4]
    # 연도 에러 처리
    try:
        invoice_year = invoiceDate.year
    except ValueError:
        print("Occurred Error: {}".format(invoiceDate))
        continue

    if invoice_year != 2011:
        continue

    # 상품 가짓수를 고려하므로 상품 코드를 셋으로 저장
    user_product_dict.setdefault(user_code, set())
    user_product_dict[user_code].add(product_id)

    product_user_dict.setdefault(product_id, set())
    product_user_dict[product_id].add(user_code)

    product_id_name_dict[product_id] = product_name

# 각 사용자가 구매한 상품 가짓수로 리스트 생성
product_per_user_li = [len(x) for x in user_product_dict.values()]

# 상품 가짓수가 1인 사용자 id
min_product_user_li = [k for k, v in user_product_dict.items() if len(v) == 1]

# 구매한 상품의 가짓수가 600개 이상인 사용자 id
max_product_user_li = [k for k, v in user_product_dict.items() if len(v) >= 600]

print("# of users purchased one product:%d" % (len(min_product_user_li)))
print("# of users purchased more than 600 product:%d" % (len(max_product_user_li)))


# 찾아낸 사용자를 군집화에 사용할 user_product_dict 에서 제외
user_product_dict = {k:v for k, v in user_product_dict.items() if 1 < len(v) <= 600}

# print("# of left user:%d" % len(user_product_dict))

# 남아있는 사용자가 구매한 상품에서도 0에서 시작하는 고유 ID를 부여한다.
# 데이터셋에서 지외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에 이러한 처리를 한다.
id_product_dict = {}
for product_set_li in user_product_dict.values():
    for x in product_set_li:
        if x in id_product_dict:
            product_id = id_product_dict[x]
        else:
            id_product_dict.setdefault(x, len(id_product_dict))

# print("# of left items:%d" % len(id_product_dict))

# 사용자 id 참조를 위한 딕셔너리
id_user_dict = {}
user_product_vec_li = []

# 군집화에서 사용할 총 고유 상품 가짓수. 즉, 원-핫 인코딩으로 변활할 피처의 가짓수
all_product_count = len(id_product_dict)

for user_code, product_per_user_set in user_product_dict.items():
    # 고유 상품 가짓수를 길이로 하는 리스트 생성
    user_product_vec = [0] * all_product_count

    # id_user_dict의 길이를 이용하여 사옹자 ID를 0부터 시작하는 user_id로 바꿉니다.
    id_user_dict[len(id_user_dict)] = user_code

    # 사용자가 구매한 상품 코드를 키로 하여 user_product_vec에서의
    # 해당 상품 코드의 상품 id를 찾는다. 그리고 값을 1로 세팅
    for product_name in product_per_user_set:
        user_product_vec[id_product_dict[product_name]] = 1

    # 한 사용자의 처리가 끝났으므로 이 사용자의 user_product_vec을 배열에 추가한다.
    # 이때 배열의 인데스는 새로 정의한 user_id가 된다.
    user_product_vec_li.append(user_product_vec)

# 학습용과 평가용 데이터로 나누기 위해 사용자-상품 벡터를 셔플한다.
random.shuffle(user_product_vec_li)

# 학습용 데이터에 사용자 2500명을, 평가용 데이터에 나머지 사용자를 넣는다.
# 학습용 데이터 있는 사용자 정보만을 가지고 클러스터를 만든 후
# 평가용 데이터의 사용자가 어느 클러스터에 속하는지 알아본다.
train_data = user_product_vec_li[:2500]
test_data = user_product_vec_li[2500:]
# print("# of train data: {}, # of test_data: {}".format(len(train_data), len(test_data)))

# 학습 데이터를 군집화하여 4개의 클러스터를 생성한 후 그 결과를 km_predict에 저장한다.
km_predict = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=20).fit(train_data) # return :estimator

# km_predict 의 predict 함수를 이용하여 평가 데이터가 전 단계에서 만든 4개의 클러스터 중 어느 곳에 속하는지 확인
km_predict_result = km_predict.predict(test_data)


# ############################################################################################

"""에러가 적고 이해하기 쉬운 클러스터 개수 정하기

    - 정량적 평가로 정하기
        * 실루엣 계수 (silhouette coefficient)
            # 생성된 클러스터 안의 데이터가 얼마나 밀접하게 모여 있는지 계산
            
            s = b - a / max(a, b)
            
            a: 하나의 샘플과 그 샘플과 같은 클러스터에 있는 다른 샘플 간의 거리 평균
            b: 하나의 샘플과 그 샘플이 속한 클러스터에서 
            가장 가까운 클러스터(중심점 간의 거리가 가장 짧은 클러스터)에 있는 다른 샘플 간의 거리 평균
             
            # 실루엣 계수는 -1부터 1사이의 값을 가진다.
                계수가 1이면 자신이 속한 클러스터에 매우 유사하고
                다른 클러스터와 다르다는 것을 의미
                -1이면 위 내용의 반전이다.
                
            #사이킷 런에서 이 값을 쉽게 구할 수 있도록 
            metric 모듈의 silhouette_score 함수를 제공한다.
    - 정성적 평가로 정하기  
    
"""

from sklearn.metrics import silhouette_score
import numpy as np

test_data = np.array(user_product_vec_li)

for k in range(2, 9):
    km = KMeans(n_clusters=k).fit(test_data)
    print("score for %d clusters: %.3f" % (k, silhouette_score(test_data, km.labels_)))

# 구매 상품만으론 뚜렷한 군집화가 어려울 것 같다는 의미
# result
# score for 2 clusters: 0.345
# score for 3 clusters: 0.225
# score for 4 clusters: 0.201
# score for 5 clusters: 0.203
# score for 6 clusters: 0.181
# score for 7 clusters: 0.164
# score for 8 clusters: 0.182