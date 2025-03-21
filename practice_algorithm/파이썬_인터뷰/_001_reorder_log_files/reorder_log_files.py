def reorder_log_files(logs: [str]) -> [str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 람다 필터 - tuple(key, key)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
