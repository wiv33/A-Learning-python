# https://leetcode.com/problems/daily-temperatures


# input: [73, 74, 75, 71, 69, 72, 76, 73]
# output: [1, 1, 4, 2, 1, 1, 0, 0]

# 매일의 화씨 온도 리스트를 입력받아서,
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력

def daily_temperatures(T: []) -> []:
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        #  현재 온도가 스택 값보다 높다면 정답처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)

    return answer


if __name__ == '__main__':
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]

    assert expected == daily_temperatures(t)
