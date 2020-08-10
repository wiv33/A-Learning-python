class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        negative = False
        reverse_int = str(x).rstrip("0")[::-1]
        if x < 0:
            negative = True
            reverse_int = reverse_int.replace("-", "")

        res = int(reverse_int)
        max_int = 2 ** 31
        if res > (max_int - 1) or -res < -max_int:
            return 0

        return -res if negative else res