from unittest import TestCase

from .most_common_word import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.input_data = "Bob hit a ball, the hit BALL flew far after it was hit."
        self.banned = ['hit']

    def test_most_common_word(self):
        actual = Solution(input_data=self.input_data, banned=self.banned).most_common_word()
        self.assertEqual("ball", actual)
