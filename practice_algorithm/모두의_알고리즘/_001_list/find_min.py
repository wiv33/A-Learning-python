def find_min(arr: []) -> int:
    min_val = arr[0]
    for i in range(1, len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]

    return min_val
