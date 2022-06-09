import collections
import re


class OrderGroup:
    def __init__(self):
        self.TO_HUNDRED_MILLION: int = 100_000_000
        self.TO_THOUSAND: int = 10_000_000
        self.TO_MILLION: int = 1_000_000
        self.TO_TEN_THOUSAND: int = 10_000
        self.TO_WON: int = 1
        self.get_most_mod = lambda: '모스트 나머지'
        self.most_commission = 0.2
        self.commission_ = (1.0 - self.most_commission)
        self.interest = lambda money, inter: int(money * self.commission_ * inter)

        self.unit_map = {'억': self.TO_HUNDRED_MILLION,
                         '천': self.TO_THOUSAND,
                         '백만': self.TO_MILLION,
                         '만': self.TO_TEN_THOUSAND,
                         '원': self.TO_WON}
        self.most_add = []
        self.recruitment_money_groups = [
            self.recruitment_money_group(name.replace("\n", '').split(" ")[0], name.replace("\n", '').split(" ")[1], idx)
            for idx, name in enumerate(open('money_list.txt').readlines())]
        self.first_come_names = []
        self.filter_first_come_group()
        self.expected_total_money = sum([int(x[0]) for x in self.recruitment_money_groups]).__format__(',')
        for idx, k, price in self.most_add:
            print(idx, k, price)
            print(self.recruitment_money_groups)
            self.recruitment_money_groups.__getitem__(idx)[1].append((self.get_most_mod(), f"{price}"))

    def filter_first_come_group(self):
        for x in open('names.txt').readlines():
            group = self.clean_first_come_group(x)
            if group is not None:
                self.first_come_names.append(group)

    def to_regular_money(self, money, i=None):
        if money == '':
            return 0

        clean_money = re.sub('[^0-9억천백만원,.]', '', money)
        extract_unit = re.search('(백만)|[억천만원]', clean_money)
        if not extract_unit:
            return int(clean_money) * self.unit_map.get('만')

        extract_money = float(re.sub('[^0-9.]', '', clean_money))
        regular_money = int(extract_money * self.unit_map.get(extract_unit.__getitem__(0)))
        if regular_money % self.unit_map['백만'] != 0:
            self.most_add.append((i, regular_money, regular_money % self.unit_map['백만']))

        return regular_money

    def clean_first_come_group(self, names):
        full_split = re.split('[ ]', names.replace('\n', ''))

        money = full_split[full_split.__len__() - 1]
        if not re.sub('[^0-9]', '', money).isdigit():
            return None

        # print(name, self.to_regular_money(money))
        return ''.join(full_split[1:full_split.__len__() - 1]).split("/")[0], self.to_regular_money(money)

    def recruitment_money_group(self, money, interest=0.003, i=None):
        return self.to_regular_money(money, i), [], interest

    def result(self):
        # print(self.recruitment_money_groups)
        # print(self.expected_total_money)
        # print(self.first_come_names)

        for money, groups, interest in self.recruitment_money_groups:
            expected_to_money = 0
            most_add = []
            for n, m in groups:
                money -= int(m)

            while expected_to_money < money:
                if len(self.first_come_names) < 1:
                    groups.append((self.get_most_mod(), money))
                    return self.recruitment_money_groups

                user_name, user_money = self.first_come_names.pop(0)
                u_money = int(user_money)
                expected_to_money = self.mod_most_add(expected_to_money, most_add)

                sum_money = u_money + expected_to_money
                if money < sum_money:
                    final_money = money - expected_to_money
                    expected_to_money += final_money
                    groups.append((user_name, final_money))
                    self.first_come_names.insert(0, (user_name, u_money - final_money))
                    break

                expected_to_money += u_money
                groups.append((user_name, u_money))

            for most in most_add:
                groups.append(most)

        return self.recruitment_money_groups

    def mod_most_add(self, expected_to_money, most_add, is_add=False):
        if is_add and expected_to_money % self.unit_map['백만'] != 0:
            mod_money = expected_to_money % self.unit_map['백만']
            most_mod_money = self.unit_map['백만'] - mod_money
            expected_to_money += most_mod_money
            most_add.append((self.get_most_mod(), most_mod_money))
        return expected_to_money


if __name__ == '__main__':
    orderGroup = OrderGroup()
    print('모집 총 금액', orderGroup.expected_total_money)
    print("=" * 33)
    for result in orderGroup.result():
        print(f"모집 금액: {format(result[0], ',')}, 수수료: {result[2]}")
        for i, x in enumerate(result[1], 1):
            name = x[0]
            first_come_money = int(x[1])
            apply_money = int(first_come_money / orderGroup.unit_map["만"])
            interest = orderGroup.interest(first_come_money, float(result[2])).__format__(",")
            print(f'{i}. {name} {apply_money}만, {interest}원')

        print("=" * 33)
