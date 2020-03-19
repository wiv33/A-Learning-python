"""
KMeans 클래스

class sklearn.cluster.KMeans(n_clusters=8, init='kmeans++', n_init=10,
                        max_iter=300, tol=0.0001, precompute_distances='auto',
                        verbose=0, random_state=None, copy_x=True, n_jobs=1)

:n_clusters
    클러스터 수, 기본값은 8
:n_init
    클러스터 중심의 촉화 횟수. 기본 값은 10
    - k-평균은 초기 중심점을 어디로 잡느냐에 따라 클러스터의 모양이 바뀔 수 있다.
    따라서 여러 번 중심점을 선택하여 각 샘플로부터 중심점까지의 거리의 총합이 가장 낮은
    클러스터 결과를 반환한다.
    ex) n_init을 10으로 설정하면 중심점을 10번 골라 10번의 kmeans를 실행한다
:max_iter
    중심점의 최대 업데이트 수. default 300
    수렴하지 않아도 이 값만큼 중심점을 갱신하면 알고리즘이 종료된다.
:tol
    tolerance. 중심점 판단 시에 사용하는 값. 기본값 0.0001
    예전 중심점과 갱신된 중심점의 차이가 tol보다 작을 경우 완벽히 같지 않아도
    수렴했다고 판단하고 갱신을 종료한다.
init: 초기 중심점의 선택 방식. default kmeans++
    random, kmeans++, 사용자 정의 함수 가능.
    kmeans는 샘풀 수와 특징 벡터의 차원 수에 따라 계산 시간이 선형으로 증가.
    이를 해결하기 위해 초기 중심점을 가급적 떨어진 샘플로 고르는 kmeans++가 제안되었다.

군집화 종류 후 다음 값을 참조할 수 있다.

:cluster_centers_
    중심점 피처값 벡터의 리스트
:labels_
    각 샘플의 클러스터 ID
:inertia_
    각 샘플과 그 샘플이 속하는 클러스터의 중심까지의 거리의 총합

===

샘플이 학습 데이터를 이용하여 생성된 클러스터 중 어디에 속하는지 예측하는 함수
predict(X)

:X
    2차원 배열형의 새로운 데이터.
    이때 입력 데이터의 피처 수가 학습(fit 함수)에 사용한 데이터의 피처 수와 같아야 한다.
    X 안의 샘플이 속하는 클러스터의 ID를 리스트로 반환한다.

"""
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

print("# of left user:%d" % len(user_product_dict))

# 남아있는 사용자가 구매한 상품에서도 0에서 시작하는 고유 ID를 부여한다.
# 데이터셋에서 지외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에 이러한 처리를 한다.
id_product_dict = {}
for product_set_li in user_product_dict.values():
    for x in product_set_li:
        if x in id_product_dict:
            product_id = id_product_dict[x]
        else:
            id_product_dict.setdefault(x, len(id_product_dict))

print("# of left items:%d" % len(id_product_dict))

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
print("# of train data: {}, # of test_data: {}".format(len(train_data), len(test_data)))

# 학습 데이터를 군집화하여 4개의 클러스터를 생성한 후 그 결과를 km_predict에 저장한다.
km_predict = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=20).fit(train_data) # return :estimator

# km_predict 의 predict 함수를 이용하여 평가 데이터가 전 단계에서 만든 4개의 클러스터 중 어느 곳에 속하는지 확인

km_predict_result = km_predict.predict(test_data)
print(km_predict_result)

# 0번째 평가 샘플이 클러스터 1번에 속하고, 1번재 평가 샘플이 클러스터 3번에 속한다는 것을 알 수 있다.
# result
# # of train data: 2500, # of test_data: 1233
# [3 3 2 ... 3 3 3]

