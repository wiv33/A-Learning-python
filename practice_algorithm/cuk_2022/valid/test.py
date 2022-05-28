import unittest
import logging
from ValidSolution import isValid


class MyTestCase(unittest.TestCase):
    def test_true(self):
        true_list = ['()', "()[]{}", '((()))', '()', "([)]", "({[)]}", "{({[)]}}", "(){{[[]}}]"]
        for i, x in enumerate(true_list):
            try:
                self.assertTrue(isValid(x))
            except Exception as e:
                print(i, x)
                self.assertTrue(isValid(x))
                self.assertIsNotNone(e)

    def test_false(self):
        false_list = ["((())", "(]", "((]}", "(}]}", "}{][", "{][}", "}{][", "(}){", "(}[){]", "({]})["]
        for i, x in enumerate(false_list):
            try:
                self.assertFalse(isValid(x))
            except Exception as e:
                print(i, x)
                self.assertFalse(isValid(x))
                self.assertIsNotNone(e)

    def test_temp_true(self):
        self.assertTrue(isValid("([)]"))
        self.assertTrue(isValid("({[})]"))
        self.assertTrue(isValid("([{[})]]"))
        self.assertTrue(isValid("{{{[[(})]}}]"))


if __name__ == '__main__':
    unittest.main()
