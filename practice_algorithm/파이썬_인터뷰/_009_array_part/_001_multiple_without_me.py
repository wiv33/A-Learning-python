from unittest import TestCase


def multiple_without_me(data: [int]) -> [int]:
    result = []
    p = 1

    for i in range(len(data)):
        result.append(p)
        p = p * data[i]

    print(result)
    p = 1
    for i in range(len(data) - 1, -1, -1):
        result[i] = p * result[i]
        p = p * data[i]

    print(result)
    return result


class TestMultipleWithoutMe(TestCase):
    def test_init(self):
        self.assertEqual([60, 40, 30, 24], multiple_without_me([2, 3, 4, 5]))
