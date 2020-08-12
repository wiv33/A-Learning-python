from unittest import TestCase

from .zigzag_conversion import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.input = (3, "PAYPALISHIRING")
        self.expected = "PAHNAPLSIIGYIR"

    def test_convert(self):
        actual = Solution().convert(s=self.input[1], numRows=3)
        self.assertEqual(self.expected, actual)
