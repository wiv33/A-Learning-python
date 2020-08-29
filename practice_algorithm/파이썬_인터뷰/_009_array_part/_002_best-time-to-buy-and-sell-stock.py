import sys


def max_profit(prices: [int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(max_price, prices[j] - price)

    return max_price


def max_profit_(prices: [int]) -> int:
    profit = 0
    # profit = -sys.maxsize
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit


result = max_profit([7, 1, 5, 3, 6, 4])
assert result == 5

res = max_profit_([7, 1, 5, 3, 6, 4])
assert res == 5
