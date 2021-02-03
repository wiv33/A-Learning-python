def is_match(s: str, p: str) -> bool:
    if p == ".*":
        return True

    for i, x in enumerate(p):
        print(i, x)

    return s == p


