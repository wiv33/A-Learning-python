import unittest

from .zigzag_conversion import Solution


class TestSolution(unittest.TestCase):
    def test_solution_convert(self):
        actual = Solution().convert(s="PAYPALISHIRING", numRows=3)
        self.assertEqual("PAHNAPLSIIGYIR", actual)

    def test_PAYPALISHIRING(self):
        actual = Solution().convert(s="PAYPALISHIRING", numRows=2)
        self.assertEqual("PAHNAPLSIIGYIR", actual)

    def test_praiiyhnpsgail(self):
        actual = Solution().convert(s="PAYPALISHIRING", numRows=6)
        self.assertEqual("PRAIIYHNPSGAIL", actual)


if __name__ == '__main__':
    unittest.main()
