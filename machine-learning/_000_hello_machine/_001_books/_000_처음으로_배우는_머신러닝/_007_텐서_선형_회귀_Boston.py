"""
ref: _000_Boston_dataset

학습과정
    1. 데이터 입력을 위한 플레이스홀더 정의
    2. 학습에 사용할 파라미터를 변수형으로 정의
    3. 모델, 손실함수, 최적화함수 정의
    4. 세션 시작
    5. 변수 초기화 선언
    6. 데이터 피딩
    7. 최적화함수 실행

    *시각화
"""
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt  # 학습 결과 플롯용 패키지
from sklearn import datasets

boston = datasets.load_boston()
boston_slice = [x[5] for x in boston.data]

# 텐서플로에서 사용할 크기로 조정
# reshape 함수로 데이터를 열이 1인 배열형으로 변환
data_x = np.array(boston_slice).reshape(-1, 1)  # == np.array(boston_slice).reshape(506, 1)
data_y = boston.target.reshape(-1, 1)
# data_x.shape == data_y.shape: True

""" 
선형 회귀
    y = wx + b
    입력 데이터(x) * 기울기(w) + 편향(b, 절편이라고도 한다) = 타깃 데이터(y)가 되는 
    기울기와 편향을 찾는 것이 목표 
    
학습 전에는 기울기와 편향을 알 수 없기 때문에 0으로 설정한 후 최적화를 통해 학습한다.
"""