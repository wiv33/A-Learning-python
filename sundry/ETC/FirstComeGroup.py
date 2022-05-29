import collections
import re


class OrderGroup:
    def __init__(self):
        self.TO_HUNDRED_MILLION: int = 100_000_000
        self.TO_THOUSAND: int = 10_000_000
        self.TO_MILLION: int = 1_000_000
        self.TO_TEN_THOUSAND: int = 10_000
        self.TO_WON: int = 1

        self.unit_map = {'억': self.TO_HUNDRED_MILLION,
                         '천': self.TO_THOUSAND,
                         '백만': self.TO_MILLION,
                         '만': self.TO_TEN_THOUSAND,
                         '원': self.TO_WON}
        self.most_add = []
        self.recruitment_money_groups = [self.recruitment_money_group(x.replace("\n", ''), i) for i, x in
                                         enumerate(open('money_list.txt').readlines())]
        self.first_come_names = []
        self.filter_first_come_group()
        self.expected_total_money = sum([int(x[0]) for x in self.recruitment_money_groups])
        for i, k, price in self.most_add:
            self.recruitment_money_groups.__getitem__(i)[1].append(("모스트", f"{price}"))

    def filter_first_come_group(self):
        for x in open('names.txt').readlines():
            group = self.clean_first_come_group(x)
            if group is not None:
                self.first_come_names.append(group)

    def to_regular_money(self, money, i=None):
        clean_money = re.sub('[^0-9억천백만원,.]', '', money)
        extract_unit = re.search('(백만)|[억천만원]', clean_money)
        if not extract_unit:
            return int(clean_money) * self.unit_map.get('만')

        extract_money = int(float(re.sub('[^0-9.]', '', clean_money)))
        regular_money = (extract_money * self.unit_map.get(extract_unit.__getitem__(0)))
        if regular_money % self.unit_map['백만'] != 0:
            self.most_add.append((i, regular_money, regular_money % self.unit_map['백만']))

        return regular_money

    def clean_first_come_group(self, names):
        full_split = re.split('[ ]', names.replace('\n', ''))

        name = ''.join(full_split[1:full_split.__len__() - 1]).split("/")[0]
        money = full_split[full_split.__len__() - 1]
        if not re.sub('[^0-9]', '', money).isdigit():
            return None

        # print(name, self.to_regular_money(money))
        return name, self.to_regular_money(money)

    def recruitment_money_group(self, money, i=None):
        return self.to_regular_money(money, i), []

    def result(self):
        print(self.recruitment_money_groups)
        print(self.expected_total_money)
        print(self.first_come_names)

        for money, group in self.recruitment_money_groups:
            expected_to_money = 0
            most_add = []
            for n, m in group:
                money -= int(m)

            print(money)
            while expected_to_money < money:
                if len(self.first_come_names) < 1:
                    return 'first_come_names is empty'

                name, user_money = self.first_come_names.pop(0)
                u_money = int(user_money)
                expected_to_money = self.mod_most_add(expected_to_money, most_add)

                sum_money = u_money + expected_to_money
                if money < sum_money:
                    final_money = money - expected_to_money
                    expected_to_money += final_money
                    group.append((name, final_money))
                    self.first_come_names.insert(0, (name, u_money - final_money))
                    # print((name, final_money))
                    break

                expected_to_money += u_money
                group.append((name, u_money))

            for most in most_add:
                group.append(most)

        return self.recruitment_money_groups

    def mod_most_add(self, expected_to_money, most_add, is_add=False):
        if is_add and expected_to_money % self.unit_map['백만'] != 0:
            mod_money = expected_to_money % self.unit_map['백만']
            most_mod_money = self.unit_map['백만'] - mod_money
            expected_to_money += most_mod_money
            most_add.append(('모스트', most_mod_money))
        return expected_to_money


if __name__ == '__main__':
    group = OrderGroup()
    for total_money, g in group.result():
        print("=" * 33)
        print(f"모집 금액: {format(total_money, ',')}")
        for i, x in enumerate(g, 1):
            print(f'{i}. {x[0]} {(int(x[1]).__format__(","))}')

        print("=" * 33)

