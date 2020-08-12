# https://leetcode.com/problems/zigzag-conversion/
import collections


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
        # tag::case 1[]
        default_dict = collections.defaultdict(list)
        # end::case 1[]

        # tag::case 2[]
        arr = [""] * numRows
        # end::case 2[]
        switch = True
        idx = 0
        print("row_nums is [{}]".format(numRows))
        for x in s:
            # tag::case 2[]
            arr[idx] += str(x)
            # end::case 2[]

            # tag::case 1[]
            default_dict[idx] += x
            # end::case 1[]
            if switch:
                idx += 1
                if idx >= numRows - 1:
                    switch = False
            else:
                if idx <= 1:
                    switch = True
                idx -= 1

        # tag::case 1[]
        result = []
        for a in default_dict.values():
            result += a
        # end::case 1[]

        # tag::case 1[]
        # return "".join(result)
        # end::case 1[]

        # tag::case 2[]
        return "".join(arr)
        # end::case 2[]


actual = Solution().convert(s="PAYPALISHIRING", numRows=6)
print("PRAIIYHNPSGAIL" == actual)
