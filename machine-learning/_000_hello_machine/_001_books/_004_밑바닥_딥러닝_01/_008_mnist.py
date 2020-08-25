import os
import sys

from dataset.mnist import load_mnist

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)


"""
신경망에서는 활성화 함수로 시그모이드와 ReLU 함수 같은 매끄럽게 변화하는 함수를 이용한다.
(곡선으로 변화하는 함수)
기계학습 문제는 크게 회귀와 분류로 나눌 수 있다.
대중적인 출력층의 활성화 함수 분류
    회귀: 항등 함수
    분류: 소프트맥스
분류에서는 출력층의 뉴런 수를 분류하려는 클래스 수와 같게 설정한다.

배치란?
입력 데이터를 묶은 것
"""