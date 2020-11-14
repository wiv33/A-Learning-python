import unittest


def a1():
    global a
    a = 20
    return a


def a2():
    return a


a = 50


def sum_range(start, cnt):
    result = 0
    for i in range(start, cnt + 1):
        result = result + i

    return result


class GlobalTest(unittest.TestCase):
    def test_is_20(self):
        self.assertEqual(a1(), a2())
        print(a1())
        print(a2())

    def test_sum(self):
        self.assertEqual(55, sum_range(1, 10))
