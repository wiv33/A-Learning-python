import unittest

from vectormodule import VectorModule


class MyTestCase(unittest.TestCase):
    def test_for_example_5(self):
        """ 벡터 a, b = [1, -1, 3], [-2, 4, 3]일 때 다음을 구하여라. """
        a, b = [1, -1, 3], [-2, 4, 3]

        module = VectorModule()
        result_a = module.plus_minus((5, a), (1, b))
        self.assertEqual([3, -1, 18], result_a.tolist())

        result_b = module.plus_minus((3, a), (8, b))
        self.assertEqual([-13, 29, 33], result_b.tolist())

        result_c = module.plus_minus((-8, a), (9, b))
        print(result_c)
        self.assertEqual([-26, 44, 3], result_c.tolist())

    def test_for_example_6(self):
        """선형결합 (일차결합, linear combination)

        Caffeine
        C8H10N4O2

        탄소 원자 8개
        수소 원자 10개
        질소 원자 4개
        산소 원자 2개

        선형들이 모여 새로운 벡터가 만들어지는 것
        벡터의 선형결합 v= 4a -2b + 3c 구하기
        """
        a, b, c = [1, -2, 1], [-1, 5, 2], [2, 0, -3],
        module = VectorModule()
        result = module.plus_minus_list([("+", 4, a), ("-", 2, b), ("+", 3, c)])
        self.assertEqual([12, -18, -9], result.tolist())

    def test_for_example_7(self):
        """ 일차 독립 (linearly independent, 선형독립)
        : 집합 {v1, v2, v3, …, Vn}가 방정식
        c1v1 + c2v2 + c3v3 … + cnvn = 0
        을 만족시키는 상수가 유일하게 c1 = c2 = c3 = … = 0뿐일 때

        v1 = k2v2 + k3v3 + … + knvn으로 표현이 가능할까?
        불가능하다.

        일차 종속 (linearly dependent, 선형종속)
        c1 = c2 = c3 = … = 0 외에도 있을 때

        v1 = k2v2 + k3v3 + … + knvn 으로 표현이 가능하다.

        """

        a, b = [2, 1, -6], [3, -2, -4],

        minus = VectorModule().plus_minus((1, a), (7, b), "-")
        print(minus)


    def test_4(self):
        a, b = [-1, -1, 3], [-1, -1, 0]
        minus = VectorModule().plus_minus((1, a), (3, b), '-')
        print(minus)

    def test_5(self):
        a = [
            [1, -2, 3],
            [2, 0, -1],
            [0, -1, 0]
        ]
        b = [
            [0, 1, -1],
            [-3, -2, 2],
            [3, 1, 0]
        ]

        a = np.array(a)
        b = np.array(b)

        a = 3 * a
        b = 2 * b

        print(a - b)

    def test_8(self):
        a = np.array([
            [1, 0, 2],
            [-1, 2, -1],
            [0, 1, 0]
        ])

        print(a ** 3)


import numpy as np

if __name__ == '__main__':
    unittest.main()
