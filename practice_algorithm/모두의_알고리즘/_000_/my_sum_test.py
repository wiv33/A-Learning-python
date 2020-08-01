import unittest

from .my_sum import my_sum, my_sum2


class MyTestCase(unittest.TestCase):
    def test_for_sum(self):
        n = 10
        actual = my_sum(n)
        self.assertEqual(385, actual)

        n = 2
        actual = my_sum(n)
        self.assertEqual(5, actual)

    def test_another(self):
        n = 10
        actual = my_sum2(n)
        self.assertEqual(385, actual)

        n = 2
        actual = my_sum2(n)
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
