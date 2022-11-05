def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        _min = heapq.heappop(scoville)
        if _min >= K: # 종료 조건
            break
        new_scov = _min + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_scov)
        answer += 1

    if len(scoville) < 2 and scoville[0] < K:
        answer = -1

    return answer


if __name__ == '__main__':
    assert 2 == solution([1, 2, 3, 9, 10, 12], 7)
