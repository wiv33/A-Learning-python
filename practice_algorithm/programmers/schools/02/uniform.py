def solution(n, lost, reserve):
    lend_dict = get_can_lend_dict(reserve)
    reserve_cnt = 0
    for student_num in lost:
        reserve_student = lend_dict.get(student_num)
        if reserve_student and reserve_student.check_can_lend(student_num):
            reserve_student.lend(student_num)
            reserve_cnt += 1

    return n - len(lost) + reserve_cnt


def get_can_lend_dict(reserve):
    from collections import defaultdict
    can_land_dict = defaultdict(ReserveStudent)
    for x in reserve:
        student = ReserveStudent(x)
        can_land_dict[x - 1] = student
        can_land_dict[x + 1] = student
    return can_land_dict


class ReserveStudent:
    def __init__(self, this_num: [int]):
        self.this = this_num
        self.prev = this_num - 1
        self.next = this_num + 1
        self.lent_num = 0
        self.can_lend = True

    def check_can_lend(self, lost_student_num: int) -> bool:
        return self.this == lost_student_num or (
                self.can_lend and (lost_student_num == self.prev or lost_student_num == self.next))

    def lend(self, lost_student_num):
        self.lent_num = lost_student_num
        self.can_lend = False


def solution2(n, lost, reserve):
    u = [1] * (n + 2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1

    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i:i + 2] = [1, 1]

    return len([x for x in u[1:-1] if x > 0])


def solution3(n, lost, reserve):
    s = set(lost) & set(reserve)  # 교집합
    l = set(lost) - s
    r = set(reserve) - s

    for x in sorted(r):
        # 체육복을 빌려줄 수 있는 학생
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    # 빌려야 하는데 빌리지 못한 학생
    return n - len(l)


if __name__ == '__main__':
    print(5 == solution(5, [2, 4], [1, 3, 5]))
    print(4 == solution(5, [2, 4], [3]))
    print(2 == solution(3, [3, 4], [1, 4]))

    print(5 == solution2(5, [2, 4], [1, 3, 5]))
    print(4 == solution2(5, [2, 4], [3]))
    print(2 == solution2(3, [3, 4], [1, 4]))

    print(5 == solution3(5, [2, 4], [1, 3, 5]))
    print(4 == solution3(5, [2, 4], [3]))
    print(2 == solution3(3, [3, 4], [1, 4]))
