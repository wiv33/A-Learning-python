def factorial(n: int) -> int:
    if n <= 1:
        return n
    # 4 -> factorial(4-1): 3 -> factorial(3-1): 2 -> factorial(2-1): 1
    # 4 * 3 * 2 * 1
    return n * factorial(n - 1)
