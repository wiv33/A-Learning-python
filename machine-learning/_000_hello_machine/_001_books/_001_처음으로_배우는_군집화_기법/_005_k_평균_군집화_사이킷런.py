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