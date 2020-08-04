def hanoi_top(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, " -> ", to_pos)
        return

    hanoi_top(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, " -> ", to_pos)

    hanoi_top(n - 1, aux_pos, to_pos, from_pos)
