"""
행렬식
라이프니츠
연립방정식의 해법을 구하기 위해 처음 고안
정방행렬 A 구하기
|A|, det(A), det A
`가역 |A| != 0`


A = [[2, 7, 1], [-2, 0, -1], [5, -3, 2]]
|A| = -7

1 / 0 = 계산 불가
"""

import numpy as np


class Determinant:
    """
    행렬식

    정방행렬 A를 특정한 방법으로 계산하여 얻게 되는 함숫값
    1. 정방인지 (2,2) or (3,3) or (n,n)
    2. 분모가 > 0인지  (ad - bc) != 0
    3. 사루스
    """

    def __init__(self, arr: [float], debug_flag: bool = True):
        self.origin_matrix: np = np.array(arr)
        self.origin_shape: (int, int) = self.origin_matrix.shape
        self.matrix: np = self.origin_matrix.copy()
        self.shape: (int, int) = self.matrix.shape
        self.validation: Validation = Validation(self)
        self.debug_on = debug_flag
        # pretty print
        np.set_printoptions(suppress=True)
        self.perforation = "=" * 33

        if not self.is_reversible_determinant():
            print("not available determinant")
            raise Exception()

    def is_reversible_determinant(self):
        """ 정사각행렬, 가역이 0이 아닌지 체크 """
        return self.validation.is_reversible_determinant()

    def cofactor(self, cofactor_ij: (int, str)):
        """
        여인수 :: 부호 바꾸기
        Cij = + - Mij
        원소 i + j가 짝수면 +, 홀수면 -
        (start index 1)
        [
            [+ - +],
            [- + -],
            [+ - +]
        ]

        """
        determinant = self.semi_determinant()
        return determinant if sum(cofactor_ij) % 2 == 0 else (-determinant[0], determinant[1])

    def final_result(self, selected_row: int = 0):
        result = []
        for x in range(len(self.origin_matrix[selected_row])):
            # print(self.matrix[selected_row, x])
            # print(self.cofactor((selected_row, x)))
            if 0 == self.origin_matrix[selected_row, x]:
                # print("x is zero", self.origin_matrix[selected_row, x])
                continue
            cofactor_shape = (selected_row, x)
            self.minor_determinant(cofactor_shape)
            cofactor = self.cofactor(cofactor_shape)
            print("cofactor :", cofactor)
            temp_element = self.origin_matrix[selected_row, x] * cofactor[0]
            if self.debug_on:
                print(f"(a{selected_row}{x} = {self.origin_matrix[selected_row, x]})"
                      f" * (m{selected_row}{x} = {cofactor[1]})")
            result.append(temp_element)

        return sum(result)

    def minor_determinant(self, deleted_by):
        """
        라이프니츠의 소행렬식
        deleted_by (행, 열)을 제거한 후 계산
        """

        deleted = np.delete(self.origin_matrix, deleted_by[0], axis=0)
        self.matrix = np.delete(deleted, deleted_by[1], axis=1)
        self.shape = self.matrix.shape

        if self.debug_on:
            print(f"origin matrix: \n{self.origin_matrix}\n"
                  f"result matrix: \n{self.matrix}\n{self.perforation}")

    def semi_determinant(self) -> tuple:
        """ 결과 출력 """
        if (2, 2) == self.shape:
            return self.two_by_two()
        elif (3, 3) == self.shape:
            return self.sarrus_three_by_three()
        else:
            return self.sarrus2_n_by_n()

    def two_by_two(self) -> tuple:
        return (self.matrix[0][0] * self.matrix[1][1]
                - (self.matrix[0][1] * self.matrix[1][0])), \
               f"{' * '.join(map(str, [self.matrix[0][0], self.matrix[1][1]]))} - " \
               f"{' * '.join(map(str, [self.matrix[0][1], self.matrix[1][0]]))}"

    def sarrus_three_by_three(self) -> (float, str):
        plus_rows = (self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]) + \
                    np.prod(self.matrix.diagonal()) + \
                    (self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0])

        minus_rows = (self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]) + \
                     (self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]) + \
                     (self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1])
        return plus_rows - minus_rows, \
               f"([[{plus_rows - minus_rows}]]::[{plus_rows}]::" \
               f"{' * '.join(map(str, [self.matrix[0][2], self.matrix[1][0], self.matrix[2][1]]))} + " \
               f"{' * '.join(map(str, self.matrix.diagonal()))} + " \
               f"{' * '.join(map(str, [self.matrix[0][1], self.matrix[1][2], self.matrix[2][0]]))}" \
               f") - ([{minus_rows}]::" \
               f"{' * '.join(map(str, [self.matrix[0][1], self.matrix[1][0], self.matrix[2][2]]))}" \
               f"{' * '.join(map(str, [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]]))}" \
               f"{' * '.join(map(str, [self.matrix[0][0], self.matrix[1][2], self.matrix[2][1]]))}" \
               f")"

    def sarrus2_n_by_n(self) -> (float, str):
        """"""
        expend_rows = self.matrix[:, 0:len(self.matrix[0]) - 1]
        dummy_matrix = np.concatenate([self.matrix, expend_rows], axis=1)

        plus_rows = []
        minus_rows = []

        plus_logs = []
        minus_logs = []
        col = np.arange(start=len(self.matrix), stop=0, step=-1)
        # print(dummy_matrix, end="\ndummy =======\n\n")

        for i in range(len(dummy_matrix)):
            plus_multiply_rows = []
            minus_multiply_rows = []
            for j, r in enumerate(col):
                plus_multiply_rows.append(dummy_matrix[j][i + j])
                reverse_idx = r + i - 1
                minus_multiply_rows.append(dummy_matrix[j][reverse_idx])

            plus_logs.append(' * '.join(map(str, plus_multiply_rows)))
            minus_logs.append(' * '.join(map(str, minus_multiply_rows)))

            plus_rows.append(np.prod(plus_multiply_rows))
            minus_rows.append(np.prod(minus_multiply_rows))

        plus_result = np.sum(plus_rows)
        minus_result = 0
        for x in range(len(minus_rows)):
            minus_result -= minus_rows[x]
        # print(plus_result, minus_result)
        return plus_result + minus_result, \
               f"[[{plus_result + minus_result}]]::([{plus_result}]::{' + '.join(plus_logs)}) " \
               f"- ([{minus_result}]::{' + '.join(minus_logs)})",

    def ad_joint(self):
        """ 딸림행렬 구하기 """
        result = np.zeros(self.origin_shape)
        for x in range(self.origin_shape[0]):
            for j in range(self.origin_shape[1]):
                self.minor_determinant((x, j))
                result[x][j] = self.cofactor((x, j))[0]

        if self.debug_on:
            print("ad_joint result == ", result.T)

        return result.T


class Validation:
    def __init__(self, det: Determinant):
        self.determinant: Determinant = det

    def is_reversible_determinant(self):
        return self.is_square_matrix() and self.not_zero()

    def is_square_matrix(self) -> bool:
        return self.determinant.shape[0] == self.determinant.shape[1]

    def not_zero(self) -> bool:
        if (2, 2) == self.determinant.shape:
            two = self.determinant.two_by_two()
            return 0 != two
        elif (3, 3) == self.determinant.shape:
            three = self.determinant.sarrus_three_by_three()
            return 0 != three
        else:
            n = self.determinant.sarrus2_n_by_n()
            return 0 != n


if __name__ == '__main__':
    pass
