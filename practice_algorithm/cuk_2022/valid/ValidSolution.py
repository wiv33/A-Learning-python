class Validation:
    def __init__(self, s: str):
        assert len(s) != 0

        self.arr_for_open = []
        self.s = s
        self.is_odd = lambda: len(self.s) % 2 != 0
        self.is_empty_open_arr = lambda: len(self.arr_for_open) == 0
        self.is_contains_open_arr = lambda o: self.arr_for_open.__contains__(o)
        self.is_open = lambda c: c in '({['
        self.get_target_open = lambda close_char: {')': '(', '}': '{', ']': '['}[close_char]
        self.get_last = lambda: self.arr_for_open.__getitem__(self.arr_for_open.__len__() - 1)

    def result(self) -> bool:
        if self.is_odd():
            return False

        for x in self.s:
            if self.is_open(x):
                self.arr_for_open.append(x)
            elif self.is_diff(x):
                return False

        return self.is_empty_open_arr()

    def is_diff(self, close_char) -> bool:
        if self.is_empty_open_arr():
            return False

        target_open = self.get_target_open(close_char)
        if self.is_contains_open_arr(target_open) and self.get_last() != target_open:
            return target_open != self.pop_change_element(target_open)

        return target_open != self.arr_for_open.pop()

    def pop_change_element(self, target_open):
        for x in self.arr_for_open:
            if x == target_open:
                self.arr_for_open.remove(x)
                return x

        raise Exception('error not found in change_element')


def isValid(s):
    return Validation(s).result()
