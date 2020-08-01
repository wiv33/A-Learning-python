def find_same_name(arr: []) -> set:
    result = set()
    length = len(arr)

    for i in range(0, length - 1):
        print(f'i: {i}, val: {arr[i]}')
        for j in range(i + 1, length):
            print(f'    j: {j}, val: {arr[j]}')
            if arr[i] == arr[j]:
                print(f'add: {arr[i]}')
                result.add(arr[i])
    return result
