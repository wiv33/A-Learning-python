# https://leetcode.com/problems/zigzag-conversion/
import collections


class Solution:
    """

        EXPECTED 1

        numRows = 3

        P A Y P A L I S H I R I N G
        0       0       0       0 1
          1   1   1   1   1   1
            2       2       2

        PAHNAPLSIIGYIR


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
        default_dict = collections.defaultdict(list)
        nums = numRows
        for i, x in enumerate(s):
            d, m = divmod(i, numRows)

            print(i, d, m, x, d % 2 == 0, end='\n')
            # if d % 2 == 1:
            #     print()
            # else:

            default_dict[m].append(x)
            # print(i, x)

        print(default_dict, end="\n")
        for x in default_dict:
            if x % 2 == 0:
                print(default_dict[x])
            else:
                default_dict[x].reverse()
                print(default_dict[x])
        return 'PAHNAPLSIIGYIR'
