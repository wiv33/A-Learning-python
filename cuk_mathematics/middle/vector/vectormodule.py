import numpy as np


class VectorModule:
    """ 벡터 스칼라 배, 덧셈, 뺄셈 """
    def __init__(self):
        pass

    @staticmethod
    def plus_minus(arr1: (int, []), arr2: (int, []), sign: str = "+") -> np:
        a = (arr1[0], np.array(arr1[1])) if arr1[0] else (1, np.array(arr1[1]))
        b = (arr2[0], np.array(arr2[1])) if arr2[0] else (1, np.array(arr2[1]))

        to1 = np.broadcast_to(a[0], a[1].shape)
        to2 = np.broadcast_to(b[0], b[1].shape)
        result_a = to1 * a[1]
        result_b = to2 * b[1]

        if sign.__eq__("-"):
            return np.add(result_a, -result_b)

        return np.add(result_a, result_b)

    @staticmethod
    def plus_minus_list(tuple_list: [(str, int, [])]) -> np:
        result = np.zeros(len(tuple_list[0][2]))
        for sign, multiple, vector in tuple_list:
            arr = np.array(vector)
            to = np.broadcast_to(multiple, arr.shape)

            multiple_result = to * arr
            multiple_result = multiple_result if sign.__eq__("+") else -multiple_result
            result = np.add(result, multiple_result)

        return result



