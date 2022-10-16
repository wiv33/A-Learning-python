import math
import numpy as np


class Vector7:
    def __init__(self, vector, multiple=1):
        self.vector = vector
        self.multiple = multiple

    def get_norm(self):
        """ 벡터의 길이를 구하기
        a = (a1, a2) 이면
        ||a|| = root a1^2 + a2^2

        a = (a1, a2, a3) 이면
        ||a|| = root a1^2 + a2^2 a3^3

        """
        result = []
        vector = self.vector

        for x in vector:
            result.append(x ** 2)

        norm = np.array(result).sum()
        print(f"root: {norm}")
        return np.sqrt(norm)

    def is_one_norm(self):
        """ 단위 벡터
        :norm 이 1인 u 벡터 ||u|| == 1
        특정 벡터가 있을 때 방향은 똑같은데 길이만 1로 만들고 싶을 때가 있음.
        """
        return 1 == self.get_norm()

    def to_unit_norm(self):
        norm = self.get_norm()
        return norm / norm
