from unittest import TestCase

from hanoi_top import hanoi_top


class Test(TestCase):
    def test_hanoi_top(self):
        print("n = 1")
        hanoi_top(1, 1, 3, 2)
        print("n = 2")
        hanoi_top(2, 1, 3, 2)
        print("n = 3")
        hanoi_top(3, 1, 3, 2)
        print("n = 4")
        hanoi_top(4, 1, 3, 2)
        print("n = 5")
        hanoi_top(5, 1, 3, 2)

        # print("n = 20")
        # print(20, 1, 3, 2)

print(2 ** 20 - 1)
# 1048575
