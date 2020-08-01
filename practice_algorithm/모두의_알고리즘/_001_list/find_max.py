def find_max(arr: []) -> int:
    n = len(arr)
    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val
