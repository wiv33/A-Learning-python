from datetime import date, timedelta
import datetime


# [브론즈 기간, 실버 기간, 골드 기간, 플래티넘 기간, 다이아몬드 기간] 순서로 채워서 반환

# required fuc
# 1. full date를 넣으면 day로 환산한 일자를 반환
# 2. grade를 계산

def calc_after_minus_before(after, before):
    before_date = date.fromisoformat(before.split()[0].replace('/', '-'))
    after_date = date.fromisoformat(after.split()[0].replace('/', '-'))

    expire_date = after_date - before_date
    if expire_date.days > 30:
        return False

    return True


def calc_days(params):
    result = []
    for i in range(1, len(params) - 1, 1):
        # 1부터 마지막까지
        _before = params[i]
        _after = params[i + 1]
        isAccumulate = calc_after_minus_before(_after, _before)
        if isAccumulate:
            int(_before[i].split()[1]) + int(_after[i].split()[1])

    return result


def add_grade_day(grade_idx, price):
    pass


def solution(purchase):
    answer = []
    # insert expire date, init date, payment_money
    grade_info = calc_days(purchase)
    print(grade_info)
    return answer


if __name__ == '__main__':
    print(solution(
        ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]) == [
              245, 30, 30, 30, 30])
