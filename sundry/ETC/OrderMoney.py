import re
import collections


def result(arr, total_price):
    print(arr)
    total_money_unit = to_unit(total_price)
    print(f"total money : {total_money_unit}")

    report = collections.defaultdict()
    total_money = 0
    for x in arr:
        series = x.split(" ")
        length = len(series) - 1
        name, money = clean_name(series[1]), to_digital(clean_name(series[1]), series[length].replace('\n', ''))

        if total_money >= total_money_unit:
            break

        if total_money_unit < (total_money + money):
            final_money = total_money_unit - total_money
            total_money += final_money
            report.update({name: str(int(final_money / 10000)) + "만"})
            print(name, str(int(final_money / 10000)) + "만", total_money)
            break

        total_money += money
        report.update({name: str(int(money / 10000)) + "만"})
        print(name, str(int(money / 10000)) + "만", total_money)

    return report


def clean_name(s: str):
    if re.search('[/]', s):
        return s[:s.find("/")]
    return s


def to_digital(name, s: str) -> int:
    number = to_unit(s)
    return number


def to_unit(str_num: str) -> int:
    TO_HUNDRED_MILLION = 10_000_000
    TO_THOUSAND = 10_000_000
    TO_TEN_THOUSAND = 10_000

    if not re.search("[억천만]", str_num):
        return int(str_num) * TO_TEN_THOUSAND

    if re.search("억", str_num):
        first, second = re.split("[.,]", str_num)
        if len(second) - 1 > 1:
            return int(remove_str(str_num)) * int(TO_HUNDRED_MILLION / 10)

        return int(remove_str(str_num)) * TO_HUNDRED_MILLION

    if re.search("천", str_num):
        return int(remove_str(str_num)) * TO_THOUSAND

    if re.search('만', str_num):
        return int(remove_str(str_num)) * TO_TEN_THOUSAND


def remove_str(str_num):
    if len(str_num) == 1:
        return 1000
    return re.sub('[억천만.,]', '', str_num)


if __name__ == '__main__':
    res = [x for x in open("./names.txt").readlines()]
    total = open('total_price.txt').read()
    print(result(res, total))
