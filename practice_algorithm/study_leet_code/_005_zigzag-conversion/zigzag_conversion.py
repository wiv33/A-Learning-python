# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    """

        EXPECTED 1

        numRows = 3

        P A Y P A L I S H I R I N G
        0       0       0       0
          1   1   1   1   1   1   1
            2       2       2

        PAHN APLSIIG YIR


--
        EXPECTED 2

        numRows = 4

        P A Y P A L I S H I R I N G
        1           1           1
          2       2   2       2   2
            3   3       3   3
              4           4

        PINALSIGYAHRPI
--

        EXPECTED 3

        numRows = 6

        P A Y P A L I S H I R I N G
        1                   1
          2               2   2
            3           3       3
              4       4           4
                5   5
                  6

        PRAIIYHNPSGAIL
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        arr = [""] * numRows
        switch = True
        idx = 0
        for x in s:
            arr[idx] += str(x)
            if switch:
                idx += 1
                if idx >= numRows - 1:
                    switch = False
            else:
                if idx <= 1:
                    switch = True
                idx -= 1

        return "".join(arr)


actual = Solution().convert(s="PAYPALISHIRING", numRows=6)
print("PRAIIYHNPSGAIL" == actual)
