from unittest import TestCase

from vector7 import Vector7


class TestVector7(TestCase):
    def test_get_norm(self):
        norm = Vector7([3, 4]).get_norm()
        self.assertEqual(5, norm)

        a = [1, -2]
        print(Vector7(a).get_norm())

        a = [3, -2, 4]
        print(Vector7(a).get_norm())

    def test_for_example_2(self):
        a = [3, -2, 4]
        self.assertEqual(1, Vector7(a).to_unit_norm())

    def test_for_example_3(self):
        """ 벡터 a 상수배 후 norm 구하기 """
        a = [1, -2]
        norm = Vector7(a, 2).get_norm()
        print(norm)

