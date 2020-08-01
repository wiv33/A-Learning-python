def my_sum(n: int):
    result = 0
    for x in range(n + 1):
        result += x ** 2
    return result


def my_sum2(n: int):
    return (n * (n + 1) * (2 * n + 1)) // 6
