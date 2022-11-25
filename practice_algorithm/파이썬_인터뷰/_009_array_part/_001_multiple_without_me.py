# https://leetcode.com/problems/product-of-array-except-self
from unittest import TestCase


def multiple_without_me(data: [int]) -> [int]:
    acc = []
    p = 1

    for i in range(len(data)):
        acc.append(p)  # 자기 값은 제외하고
        p = p * data[i]  # 왼쪽부터 누적 p 곱셈

    p = 1
    for i in range(len(data) - 1, -1, -1):
        acc[i] = p * acc[i]  # 누적 p에 왼쪽부터 곱셈된 값으로 update
        p = p * data[i]  # 누적 p 오른쪽부터 누적시키기

    return acc


class TestMultipleWithoutMe(TestCase):
    def test_init(self):
        self.assertEqual([24, 12, 8, 6], multiple_without_me([1, 2, 3, 4]))


if __name__ == '__main__':
    TestCase().run()
