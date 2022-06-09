import re
import collections


def result(arr, money_list_param):
    print(arr, '\n')
    to_unit_money_list = [to_unit(x) for x in money_list_param if x.rstrip()]
    print(to_unit_money_list)
    total_money_unit_sum = sum(to_unit_money_list)

    print(f"total money : {total_money_unit_sum.__format__(',')}", '\n')

    report = collections.defaultdict()
    total_money = 0
    for i, x in enumerate(arr, 1):
        series = x.split(" ")
        length = len(series) - 1
        money_string = series[length].replace('\n', '')
        if not re.sub('[\\D]', '', money_string).isdigit():
            continue

        name, money = clean_name(series), to_digital(money_string)
        if total_money >= total_money_unit_sum:
            break


        if total_money_unit_sum < (total_money + money):
            final_money = total_money_unit_sum - total_money
            total_money += final_money
            report.update({name: str(int(money / 10000)) + "만"})
            print(f"{i}.{name} {(int(final_money / 10000)).__format__(',')}만")
            break

        total_money += money
        report.update({name: str(int(money / 10000)) + "만"})
        print(f"{i}.{name} {(int(money / 10000)).__format__(',')}만")

    return report


def clean_name(series: []):
    s = re.sub('[\n]', '', ''.join(series[1: series.__len__()]))
    if re.search('[/]', s):
        return s[:s.find("/")]
    return s


def to_digital(s: str) -> int:
    number = to_unit(s)
    return number


def to_unit(str_num_origin: str) -> int:
    TO_HUNDRED_MILLION: int = 100_000_000
    TO_THOUSAND: int = 10_000_000
    TO_TEN_THOUSAND: int = 10_000

    str_num = re.sub('[^0-9,.억천만원]', '', str_num_origin)
    search = re.search("[억천만]", str_num)

    if re.search('[^만][원]', str_num):
        return int(re.sub('[^0-9]', '', str_num))

    if not search:
        return int(str_num) * TO_TEN_THOUSAND

    unit_maps = {'억': TO_HUNDRED_MILLION,
                 '천': TO_THOUSAND,
                 '만': TO_TEN_THOUSAND}

    semi_unit = get_semi_unit(str_num, search, unit_maps)

    return int(remove_str(str_num)) * semi_unit


def get_semi_unit(str_num, search, unit_maps):
    split = re.split("[.,]", str_num)
    if len(split) <= 1:
        return unit_maps[search.__getitem__(0)]

    first, second = split
    denominator = int(f"1{('0' * (len(second) - 1))}")
    return int(unit_maps[search.__getitem__(0)] / denominator)


def remove_str(str_num):
    if len(str_num) == 1:
        return 1000
    return re.sub('[억천만.,]', '', str_num)


if __name__ == '__main__':
    res = [x for x in open("names.txt").readlines()]
    money_list = [x for x in open('money_list.txt').readlines()]
    print(result(res, money_list))
