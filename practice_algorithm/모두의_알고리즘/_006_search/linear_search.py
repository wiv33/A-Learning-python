def search_list(a: [], target: int):
    for n in range(len(a)):
        if a[n] == target:
            return n

    return -1


def search_arr(a: [], target: int):
    return [i for i in range(len(a)) if a[i] == target]


def search_name(stu_nums: [], stu_names, target: int):
    pass
