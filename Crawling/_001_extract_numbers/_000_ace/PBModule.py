import random
import json


class PB:
    """
    choice active rule
    p :power, b :basic, pc :powerball_combination, bc :basic_combination

    """

    def __init__(self, active_type="b"):
        self.rules = json.loads(open('rule.json', 'r').readline())
        self.active_type = active_type
        self.active_line = self.rules.get(self.active_type)




    def choice(self):
        pass

    def is_stop(self):
        pass


class B:
    def __init__(self, name, selector, ratio, amount):
        self.name = name
        self.selector = selector
        self.ratio = ratio
        self.amount = amount
