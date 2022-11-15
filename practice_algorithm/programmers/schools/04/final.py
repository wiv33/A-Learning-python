"""
문제 설명 세균이 증식할 수 있는 rows 행 columns 열의 칸으로 구성된 격자가 있습니다.
각 칸은 최대 max_virus 마리의 세균이 있을 수 있으며, 초 기에는 이 격자에 아무런 세균이 없습니다.
당신은 일련의 쿼리 목록을 전달받았습니다.
하나의 쿼리는 r 과 c 두 정수로 이루어져 있으며, 이는 r 행 c 열의 칸에서 " 세균 증식"을 하라는 것을 의미합니다.

세균 증식이란 다음과 같습니다.
• 만약 r 행 C 열의 칸에 있는 세균이 max virus 마리 미만이 라면, 세균을 1마리 더 늘립니다.
• 만약 r 행 c 열의 칸에 있는 세균이 max_virus 마리라면, 이 칸에 인접한 상하좌우 모든 칸에서 "세균 증식"을 시킵니다. 이때,
• 세균 증식이 여러 칸에 걸쳐서 연쇄적으로 일어날 수 있습니 다.
• 한 쿼리에서 동일한 칸에는 최대 한 번의 세균 증식만 일어 납니다. 정수 rows columns max virus , 그리고 쿼리를 의미하는 2차  원 정수 배열 queries 가 매개변수로 주어집니다.
gueries 에 들어 있는 쿼리들에 의한 세균 증식을 순서대로 실행시켰을 때, 격자의 최종 상태(각 칸에 세균이 몇 마리씩 있는지)를 2차원 정수 배열로 return 하 도록 solution 함수를 완성해주세요.

제한사항
• 1 ≤ rows , columns ≤ 20
• 1 ≤ max_virus ≤ 100
• 1 ≤ queries 의 행의 개수 ≤ 400
    o queries 의 각행은 [r,c] 2개의 정수로 이루어져 있으며, 이는 r 행 c 열에 세균 증식을 하라는 의미입니다.
    o 1 ≤ r ≤ rows
    o 1 ≤ c ≤ columns
• return 해야 하는 배열의 행 길이 = rows
• return 해야 하는 배열의 열 길이 = columns

"""


def solution(rows, columns, max_virus, queries):
    answer = [[0 for _ in range(columns)] for _ in range(rows)]

    def selector(row, col):
        stack = [(row, col)]
        visited = {row, col}

        while stack:
            i, j = stack.pop()
            if answer[i][j] < max_virus:
                answer[i][j] += 1
            else:
                for _i, _j in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= _i < rows and 0 <= _j < columns and (_i, _j) not in visited:
                        visited.add((_i, _j))
                        stack.append((_i, _j))

    for r, c in queries:
        selector(r - 1, c - 1)

    return answer


if __name__ == '__main__':
    print([[0, 2, 1, 1],
           [2, 2, 2, 1],
           [2, 2, 2, 1]] == solution(3, 4, 2,
                                     [[3, 2],
                                      [3, 2],
                                      [2, 2],
                                      [3, 2],
                                      [1, 4],
                                      [3, 2],
                                      [2, 3],
                                      [3, 1]]))
