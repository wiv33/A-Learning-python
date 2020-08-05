# 입력: 리스트
# 출력: 입력으로 주어진 리스트의 정렬

class PsSort:
    def __init__(self, arr: []):
        self.arr = arr

    def sel_sort(self):
        a = self.arr
        n = len(a)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                # if a[j[ > a[min_idx]:
                if a[j] < a[min_idx]:
                    min_idx = j
                    a[i], a[min_idx] = a[min_idx], a[i]

        return a
