import json
import re
from collections import OrderedDict
from datetime import datetime, timedelta
import logging


class FirstComeGroupV2:
    def __init__(self, money_list_plain: str, names_plain: str):
        self.TO_HUNDRED_MILLION: int = 100_000_000
        self.TO_THOUSAND: int = 10_000_000
        self.TO_MILLION: int = 1_000_000
        self.TO_TEN_THOUSAND: int = 10_000
        self.TO_WON: int = 1
        self.most_commission = 0.2
        self.commission_ = (1.0 - self.most_commission)
        self.most_interest = lambda money, inter: int(money * self.commission_ * inter)
        self.unit_map = {'억': self.TO_HUNDRED_MILLION,
                         '천': self.TO_THOUSAND,
                         '백만': self.TO_MILLION,
                         '만': self.TO_TEN_THOUSAND,
                         '원': self.TO_WON}

        self.money_group = self.init_money_group_json(money_list_plain)
        self.names = self.init_names(names_plain)
        self.exclude_names = self.init_exclude_names()
        self.set_recruitment()

    def init_money_group_json(self, money_list_plain):
        sub = re.sub('\n', '\t', open(money_list_plain).read())
        even_data = re.split('(신규)', sub)
        result = []
        for x in range(0, len(even_data), 2):
            data = even_data[x]
            if not data.strip():
                continue

            try:
                split_data = [re.sub('[)]', '', re.sub('(\t){2,5}', '\t', x)).lstrip() for x in
                              re.split('(수수료 .*%)', data) if x]
                range_date, interest, money = split_data
                dateset = self.clean_dateset(range_date)
                interest = interest, (float(re.sub('[^.\\d]', '', interest)) * 0.01)
                lender = re.sub('[ \t]{1,10}', ' ', re.sub('(\\d.*)', '', money)).strip(' ')
                extract_money = self.to_unit_money(
                    re.sub('([^\\d.억천백만]|(\\d|억|천|백|만)원)', '', [x for x in re.split('\t', money) if x][0]))
                first_list = [self.to_unit_money(x) for x in
                              [re.sub('^(\\d{1,2}.)', '', x) for x in re.split('\t', money) if x][1:] if x]

                result.append(
                    {
                        'lender': lender,
                        'sta_date': dateset['sta_date'],
                        'end_date': dateset['end_date'],
                        'diff_date': dateset['diff_date'],
                        'interest': interest,
                        'money': extract_money,
                        'names': first_list
                    })
            except Exception as e:
                print(e)
                raise Exception("occurred error !!!!", e)

        return result

    @staticmethod
    def clean_dateset(param_range_date):
        range_date = re.sub('[\t ]', '', param_range_date)
        range_date = re.sub('[^0-9월일~-]', '', range_date)
        sta, end = [x for x in re.split('[-~]', range_date) if x]
        sta = list(OrderedDict.fromkeys([x for x in re.split('(\\d{1,2}\\w)', sta) if x]))
        sta = re.sub('[월일]', '', "-".join(sta))
        sta = f'{datetime.now().year}-{sta}'
        sta = datetime.strptime(sta, "%Y-%m-%d").date()
        if '월' not in end:
            end = f'{sta.month}-{end}'
        end = re.sub('[월]', '-', re.sub('[일]', '', end))
        end = datetime.strptime(f'{sta.year}-{end}', '%Y-%m-%d').date()
        return {'sta_date': sta,
                'end_date': end,
                'diff_date': end - sta}

    def init_names(self, names_plain):
        return [self.to_unit_money(re.sub('[\n]', '', x)) for x in open(names_plain).readlines()]

    def to_unit_money(self, money: str) -> tuple:
        to_unit = ''.join(money.split(" ")[-1])
        to_unit = re.sub('[^\\d.억천백만]', '', to_unit)
        to_unit = re.sub('(천만)', '천', to_unit)

        extract_unit = re.search('(백만)|[억천만원]', to_unit)
        if not extract_unit:
            return money, self.to_actual_money(to_unit, '만')

        return money, self.to_actual_money(to_unit, extract_unit.__getitem__(0))

    def to_actual_money(self, to_unit, target_unit):
        sub = re.sub(target_unit, '', to_unit)
        if not sub:
            logging.error(f'to_unit is empty {target_unit}')
            sub = 1
        return round(float(sub) * self.unit_map.__getitem__(target_unit))

    def set_recruitment(self):
        remaining_money = 0
        for x in self.money_group:
            recruit_money, recruit_names = x['money'][1], x['names']
            if remaining_money > 0:
                logging.error(f"remaining money exists: {str(remaining_money)}")
                recruit_money += remaining_money
                remaining_money = 0

            most_add = []
            for i in range(len(recruit_names)):
                self.names.insert(0, recruit_names.pop())

            if recruit_money % self.unit_map['백만'] != 0:
                most_mod = recruit_money % self.unit_map['백만']
                recruit_money -= most_mod
                most_add.append(('모스트_나머지', most_mod))

            while recruit_money >= 0 or self.names.__len__() > 1:
                _, names_pop = self.names.pop(0)
                if len(_.split(" ")) > 2:
                    _ = ' '.join(_.split(" ")[1:])

                if not names_pop or _.split(" ")[0] in self.exclude_names:
                    continue

                if recruit_money < names_pop:
                    t = max(recruit_money, names_pop)
                    m = min(recruit_money, names_pop)

                    recruit_money = recruit_money - m
                    self.names.insert(0, (_, (t - m)))
                    recruit_names.append((_, names_pop - (t - m)))
                    break

                recruit_money -= names_pop
                recruit_names.append((_, names_pop))

            for m in most_add:
                recruit_names.append(m)

            if recruit_money > 0:
                logging.error(f"error money !! : {recruit_money}\n{x}")
        pass

    def recruitment_money_print(self):
        for x in self.money_group:
            # print(x)
            print(f"신규)\n{x['sta_date']} ~ {x['end_date']} {x['interest'][0]}\n{x['lender']}\n{x['money'][0]}\n")
            for i, z in enumerate(x['names'], 1):
                name = z[0]
                if len(name.split(" ")) > 1:
                    name = name.split(" ")[0]
                print(f'{i}. {name} {int(z[1] / self.unit_map.get("만")).__format__(",")}만')
            print()

    def to_json(self, key, obj):
        process_maps = {
            'sta_date': lambda o: {'sta_date': str(o['sta_date'])},
            'end_date': lambda o: {'end_date': str(o['end_date'])},
            'diff_date': lambda o: {'diff_date': o['diff_date'].days + 1},
            'interest': lambda o: {'interest': o['interest'][0], 'interest_actual': o['interest'][1]},
            'money': lambda o: {'money': o['money'][0], 'money_actually': o['money'][1]},
            'names': lambda o: {
                'names': [{'name': x[0], 'money': x[1],
                           'interest': self.most_interest(x[1], o['interest'][1])}
                          for x in o['names']]}
        }

        if key not in process_maps.keys():
            return {key: obj[key]}

        return process_maps[key](obj)

    def recruitment_money_to_json(self):
        result = []
        for x in self.money_group:
            obj = {}
            for z in x.keys():
                obj.update(self.to_json(z, x))
            result.append(obj)
        return result

    def init_exclude_names(self):
        result = []
        for x in [re.sub('[\n]', '', x) for x in open('exclude_names.txt').readlines()]:
            # print(' '.join(x.split(" ")[1:2]))
            result.append(' '.join(x.split(" ")[1:2]))
        print(f'exclude names : {", ".join(result)}\n')
        return result


if __name__ == '__main__':
    fg = FirstComeGroupV2('money_list_plain.txt', 'names_plain.txt')
    fg.recruitment_money_print()
    print(fg.recruitment_money_to_json())
