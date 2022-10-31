def solution(cost, order):
    print(order)
    order.sort()
    # 절댓값에서 구간 값으로 변경
    _order = [order[0]]
    for x, (m, n) in enumerate(order[1:]):
        _order.append([m - order[x][0], n])

    # 순차적으로 뒤쪽의 주문량이 더 많은 경우, 앞쪽이랑 합치는 과정
    stack = []
    for m, n in _order:
        while stack:
            _m, _n = stack[-1]
            if _m / _n < m / n:
                break
            print(f'_m({_m}) / _n({_n})({_m / _n}) < m({m}) / n({n})({m / n})')
            print(f'_n({_n}) / _m({_m})({_n / _m}) < n({n}) / m({m})({n / m})')
            stack.pop()
            m, n = m + _m, n + _n
        stack.append([m, n])

    print(stack)
    answer = 0
    for m, n in stack:
        p_prev = 0

        for t, p in cost:
            print(f'm * t({m * t}) >= n({n}) : {m * t >= n}')
            if m * t >= n:
                break
            print(answer, p,  p_prev)
            answer += (n - m * t) * (p - p_prev)  # 넘긴 갯수 * 차액
            p_prev = p

    print(answer)
    return answer


if __name__ == '__main__':
    solution([[0, 50], [50, 20], [100, 30], [200, 40]],
             [[3, 50], [7, 200], [8, 200]])
