def recursion_sum(n: int) -> int:
    if n < 1:
        return n

    return n + recursion_sum(n - 1)


def recursion_max_val(arr: []):
    length = len(arr)
    if length < 2:
        return arr[0]

    result = [arr[0]]
    for x in range(1, length - 1):
        val = arr.pop()
        if result[0] < val:
            result[0] = val

    return recursion_max_val(result)
