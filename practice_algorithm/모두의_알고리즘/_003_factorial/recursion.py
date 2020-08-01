def recursion_sum(n: int) -> int:
    if n < 1:
        return n

    return n + recursion_sum(n - 1)


def recursion_max_val(arr: []):
    if len(arr) == 1:
        return arr[0]
    return recursion_max_val([max_val for max_val in arr if arr[0] < max_val])
