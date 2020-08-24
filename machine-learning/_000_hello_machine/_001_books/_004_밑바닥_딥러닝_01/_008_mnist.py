import os
import sys

from dataset.mnist import load_mnist

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)


