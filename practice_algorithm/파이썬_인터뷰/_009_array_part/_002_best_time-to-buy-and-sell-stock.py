import sys


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# input: [7,1,5,3,6,4]
# output: 5

# 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.


def max_profit(prices: [int]) -> int:
    """
    브루트포스
    :param prices:
    :return:
    """

    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 카데인 알고리즘
def max_profit_big_o_n(prices: []) -> int:
    """
    저점과 현재 값과의 차이 계산
    :param prices:
    :return:
    """

    profit = 0  # -sys.maxsize
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == '__main__':
    assert 5 == max_profit([7, 1, 5, 3, 6, 4])
    assert 5 == max_profit_big_o_n([7, 1, 5, 3, 6, 4])
