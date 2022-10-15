import unittest

from determinant import Determinant
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_reversible_determinant_true(self):
        """
        아래 조건이 모두 True
        1. 정방행렬
        2. ad - bc != 0
        Returns
        -------

        """
        expectedTrue = Determinant([[2, 7], [-2, 0]])
        self.assertTrue(expectedTrue.is_reversible_determinant())

        sarrus = Determinant([
            [1, 3],
            [2, -4]
        ])
        self.assertTrue(sarrus.is_reversible_determinant())

    def test_three_by_three_reversible(self):
        three_by_three_is_true = Determinant([
            [1, 3, -1],
            [1, -2, 0],
            [2, -3, 4]]
        )
        self.assertTrue(three_by_three_is_true.is_reversible_determinant())

    def test_for_example_4_1(self):
        """ 다음 행렬의 소행렬식 M23 구하라 """
        M = [
            [2, 1, 4, -3],
            [0, 2, 7, -1],
            [-3, -1, 6, 1],
            [5, 2, 2, 4]
        ]
        determinant = Determinant(M)
        determinant.minor_determinant((2, 3))
        expected = [
            [2, 1, 4],
            [0, 2, 7],
            [5, 2, 2]
        ]
        self.assertListEqual(expected, determinant.matrix.tolist())

    def test_for_example_4_2(self):
        """ 예제4 다음 행렬의 행렬식을 구하여라 """
        M = [
            [2, -1, 4, 1],
            [0, 2, 0, -1],
            [-3, -1, 0, 1],
            [2, 0, 2, 1]
        ]

        print(Determinant(M).is_reversible_determinant())
        print("print result is : ", Determinant(M).final_result(1))
        self.assertEqual(22, Determinant(M).final_result(1))

    def test_for_example_5(self):
        """ 예제5 다음 행렬 A, B의 행렬식을 각각 구하고 그 값을 비교해 보시오.
         두 행의 위치 교환
        """
        A = np.array([
            [1, 3, -1],
            [-1, 2, -3],
            [2, 0, 1]
        ])

        print(A)
        # A[:, [0, 2]] = A[:, [2, 0]]  # column swap
        B = A.copy()
        B[[0, 2], :] = B[[2, 0], :]  # row swap
        self.assertFalse(np.alltrue(np.not_equal(A, B)))
        print(B)

        result_a = Determinant(A).final_result(1)
        print("=" * 333)
        result_b = Determinant(B).final_result(1)
        print("result: A", result_a)
        print("result: B ", result_b)

        self.assertTrue(result_a != result_b)
        self.assertTrue(result_a == -result_b)

    def test_for_example_6(self):
        """ 다음 행렬 A, B의 행렬식을 각각 구하고 그 값을 비교해 보시오.
        맨 마지막 행에 2 곱

        """

        A = np.array([
            [1, 1, -1],
            [-2, 2, -3],
            [2, 0, 1]
        ])

        B = A.copy()
        B[2] = 2 * B[2]

        result = Determinant(A).final_result(2)
        final_result = Determinant(B).final_result(2)

        self.assertEqual(result * 2, final_result)
        print(result)
        print(final_result)

    def test_for_example_7(self):
        """ 다음 행렬 A, B의 행렬식을 각각 구하고 그 값을 비교해 보시오.
        k^n|A|

        K = 3
        n = 3

        3 ** 3

        """

        A = np.array([
            [2, 1, -1],
            [0, 1, -2],
            [2, 1, 1]
        ])

        # |A| = 4
        # 3 * 3 * 3 == 3 ^ 3 == 27
        # 27 * 4
        B = A.copy()
        B = 3 * B

        result = Determinant(A).final_result(1)
        final_result = Determinant(B).final_result(1)
        self.assertEqual(4, result)
        self.assertEqual(3 ** 3 * result, final_result)

    def test_for_example_8(self):
        """ 다음 행렬 A의 행렬식을 구하시오.
        행교환에 해당하는 행들이 같은 경우 determinant == 0
        |B| == -|A|
        A == B
        |A| == |B| == 0

        |A| == -|A|
        2|A| == 0
        따라서 |A| == 0

        0, 1행이 같기 때문에 determinant == 0이다.

        """

        A = np.array([
            [1, -2, 6],
            [1, -2, 6],
            [-1, 5, 8]
        ])

        determinant = Determinant(A)
        result = determinant.final_result(0)
        self.assertEqual(0, result)

        result = determinant.final_result(1)
        self.assertEqual(0, result)

        result = determinant.final_result(2)
        self.assertEqual(0, result)

    def test_for_example_9(self):
        """ 다음 행렬 A, B, C 행렬식을 각각 구하고 그 값을 비교해 보시오.
        a,b,c의 1, 3행은 다 똑같고,
        두 번째 행만 다를 때, 아래 공식이 성립

        |A| + |B| = |C|

        """

        A = np.array([
            [1, 1, -1],
            [1, 2, 1],
            [1, 2, 0]
        ])

        B = A.copy()
        B[1] = [3, 1, -1]

        C = A.copy()
        C[1] = [4, 3, 0]

        print(A)
        print(B)
        print(C)

        det_a = Determinant(A).final_result(2)
        det_b = Determinant(B).final_result(2)
        det_c = Determinant(C).final_result(2)

        self.assertEqual(det_a + det_b, det_c)

    def test_for_example_10(self):
        """ 다음 행렬 A,B의 행렬식을 각각 구하고 그 값을 비교해 보시오.
        한 행에 상수 배를 한 후 다른 행에 곱하는 행연산을 수행했을 경우,
        |A| == |B|
        A, B determinant 는 같다.

        """
        A = np.array([
            [1, 2, -1],
            [-2, 3, 2],
            [0, 2, 1]
        ])

        # 0 행에 상수배 후 1 행에 더한다.
        B = A.copy()
        B[1] = B[1] + B[0] * 2.0
        print(B)

        self.assertFalse(np.alltrue(np.not_equal(A, B)))
        det_a = Determinant(A).final_result(1)
        det_b = Determinant(B).final_result()
        self.assertEqual(det_a, det_b)
        print(det_a, det_b)

    def test_for_example_11(self):
        """ 0행 (0열) 인 경우 |A| == 0
            다음 행렬 A의 행렬식을 구하시오.

            A = [
                [1, 0, -1],
                [-2, 0, 2],
                [-1, 0, 3]
            ]
        |A| == [0]((1 * 0 * 3) + (0 * 2 * -1) + (-1 * -2 * 0))
        - [0]((-1 * 0 * -1) + (0 * -2 * 3) + (1 * 2 * 0))
        == 0
        """
        A = np.array([
            [1, 0, -1],
            [-2, 0, 2],
            [-1, 0, 3]
        ])

        result = Determinant(A).final_result()
        self.assertEqual(0, result)

    def test_for_example_12(self):
        """ 단위 행렬의 행렬식은 1이다.
            다음 행렬의 행렬식을 각각 구하시오.
        """
        A = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        B = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]

        det_a = Determinant(A).final_result()
        det_b = Determinant(B).final_result()
        print(det_a, det_b)
        self.assertEqual(det_a, det_b)

    def test_for_example_13(self):
        """ 삼각행렬의 행렬식
        : 삼각행렬 A의 행렬식은 피벗의 곱
        """

        A = np.array([
            [2, -2, 4, 3, -2],
            [0, 1, 1, 5, 3],
            [0, 0, 4, 2, 2],
            [0, 0, 0, -1, 1],
            [0, 0, 0, 0, -3]
        ])

        B = np.array([
            [-3, 0, 0, 0, 0],
            [5, -3, 0, 0, 0],
            [-2, 4, 2, 0, 0],
            [5, -1, -3, 1, 0],
            [3, 2, 1, -2, 4]
        ])

        C = np.array([
            [2, 0, 0, 0, 0],
            [0, 5, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 3, 0],
            [0, 0, 0, 0, -1]
        ])

        self.assertEqual(24, np.prod(np.diagonal(A)))
        self.assertEqual(72, np.prod(np.diagonal(B)))
        self.assertEqual(-30, np.prod(np.diagonal(C)))

    def test_for_example_14(self):
        """ 행렬곱의 행렬식
        : 행렬 A와 B의 곱 AB에서 |AB| == |A||B|

        기본 행 연산에 의한 행렬식: 기본행렬 E와 행렬 A의 곱에서 |EA| = |E||A|
        1. 두 행의 위치 교환 |B| = -|A| -> |Ea| = -|I| = -1
        2. 한 행에 상수배    |B| = k|A| -> |Eb| = k|I| = k
        3. 상수배한 행을 다른 행에 더하는 것 -> |B| = |A| -> |Ec| = |I| = 1

        A = E1E2E3…En
        |AB| = |E1E2E3…EnB| = |E1||E2||E3|…|En||B|
                            = |E1E2E3…En||B| = |A||B|

        행렬 A와 B, AB에 대한 행렬식 각각 구하여 비교해 보자.

        """

        A = np.array([
            [2, 1],
            [1, 3]
        ])

        B = np.array([
            [2, 0],
            [2, -1]
        ])

        two_ = Determinant(A.dot(B)).two_by_two()[0]
        self.assertEqual(-10, two_)

        two = Determinant(A).two_by_two()
        by_two = Determinant(B).two_by_two()
        self.assertEqual(two[0] * by_two[0], two_)
        print(two, by_two)

    def test_for_example_15(self):
        """ 역행렬의 행렬식
        : 행렬 A의 역행렬 A^-1의 행렬식은
        |A^-1| = 1 / |A| = |A|^-1

        AA^-1 = I (역행렬의 정의)
        |AA^-1| = |I| = |A||A^-1| = 1

        따라서, |A^-1| = 1 / |A| = |A|^-1

        1 / x == x^-1
        역수 np.reciprocal()
        """
        from fractions import Fraction

        A = np.array([
            [1, 0, 1],
            [2, 1, 0],
            [2, 1, 2]
        ])

        A_inverse = np.array([
            [1., Fraction(1, 2), -Fraction(1, 2)],
            [-2., 0, 1.],
            [0, -Fraction(1, 2), Fraction(1, 2)]
        ])

        result = Determinant(A).final_result()
        final_result = Determinant(A_inverse).final_result()
        print(result)
        print(final_result)

    def test_for_example_16(self):
        """ 전치행렬의 행렬식
        : 행렬 A와 전치행렬 A^T

            |A| = |A^T|

        A = LU, A^T = U^TL^T (둘리틀법으로 LU 분해 시)
        |A| = |L||U|, |A^T| = |U^T||L^T|

        |L| = |L^T| = 1 이므로 (하삼각행렬, 상삼각행렬을 T해도 1임)
        |A| = |U|, |A^T| = |U^T|

        |U| = |U^T| 이므로
        |A| = |A^T|

        """

        A = np.array([
            [1, 2, -1],
            [-2, 1, 3],
            [-1, 2, 2]
        ])

        B = A.T
        self.assertEqual(1, Determinant(A).final_result())
        self.assertEqual(1, Determinant(B).final_result())

    def test_for_example_17(self):
        """ 행렬식의 기하학적 의미
        : determinant를 구하면 부피가 된다.

        원점
        (0, 0, 0)
        좌표 세 개
        (3, 0, 1)
        (1, 5, 1)
        (1, 0, 3)

        아래와 같이 열로 표현.
        """

        A = np.array([
            [3, 1, 1],
            [0, 5, 0],
            [1, 1, 3]
        ])

        self.assertEqual(40, Determinant(A).final_result())

    def test_for_example_18(self):
        """ 동차 연립선형방정식이 자명해를 가지는 조건
        : Ax = 0 에서 계수행렬 A가 가역이면, 자명해만 존재함.

        가역: |A| != 0

        |a11x1 + a12x2 + a13x3 = 0
        |a21x1 + a22x2 + a23x3 = 0
        |a31x1 + a32x2 + a33x3 = 0

        |A| = [
            [a11, a12, a13],
            [a21, a22, a23],
            [a31, a32, a33]
        ]

        = a11a22a33 + a12a23a31 + a13a21a32 - a11a23a32 - a12a21a33 != 0


        다음 동차 연립선형방정식이 자명해만을 가질 때, a의 조건을 구하시오.

        A = np.array([
            [1,   a, -2],
            [3,   6,  1],
            [-1, -2,  1]
        ])

        (1 * 6 * 1) + (a * 1 * -1) + (-2 * 3 * -2) = (6 - a + 12)
        (-2 * 6 * -1) + (a * 3 * 1) + (1 * 1 * -2) = (12 + 3a + -2)

        (6 - a + 12) - (12 + 3a + -2)
        = (-4a + 8) != 0
        = -4a != -8
        = a != 2

        """
        self.assertTrue(True)

    def test_for_example_19(self):
        """ 딸림행렬 (adjoint matrix, 수반행렬)
        : n차 정사각행렬 A의 성분에 대응하는 여인수를 성분으로 갖는 행렬의 전치행렬

        adj A

        여인수만 차 있는 전치행렬에 transpose 를 하면 `딸림행렬`이 된다.

        """

        A = np.array([
            [1, -2, 0],
            [3, 1, 2],
            [1, 2, 1]
        ])

        """
        adj A = [
            [c11 c12 c13]
            [c21 c22 c23]
            [c31 c32 c33]
        ].T
        
        = [
            [M11  -M12  M13]
            [-M21  M22 -M23]
            [M31  -M32  M33]
        ].T
        
        """

        determinant = Determinant(A)
        joint = determinant.ad_joint()
        print(joint)

    def test_for_example_20(self):
        """ ad_join 역행렬
        A(adj A) = |A|I

        A^-1 = 1 / |A| * adj A

        A(adj A) = [
            [a11 a12 a13]
            [a21 a22 a23]
            [a31 a32 a33]
        ]
        * [
            [c11 c21 c31]
            [c12 c22 c32]
            [c13 c23 c33]
        ]

        = [
            [a11C11 + a12C12 + a13C13 ,             0,                           0        ]
            [           0             , a21C21 + a22C22 + a23C23,                0        ]
            [           0             ,             0           , a31C31 + a32C32 + a33C33]
        ]

        = [
            [|A|  0    0]
            [0   |A|   0]
            [0    0  |A|]
        ]
        = |A| * [
            [1 0 0]
            [0 1 0]
            [0 0 1]
        ] = |A|I

        다음 행렬 A의 딸림행렬은 adj A = [[8, -12, -12], [-4, 8, 8], [-3, 4, 5]] 이다.
        이를 이용해 행렬 A의 역행렬을 구하시오.


        """
        from fractions import Fraction

        ad_joint_A = np.array([[8, -12, -12], [-4, 8, 8], [-3, 4, 5]])
        A = np.array([
            [2, 3, 0],
            [-1, 1, -4],
            [2, 1, 4]
        ])

        result = Determinant(A).final_result()
        res = Fraction(1, result) * ad_joint_A
        print(res)
        print(res.astype(float))


if __name__ == '__main__':
    unittest.main()
