import unittest


def main_run(func, params):
    func(params)


def solution(params):
    print('solution run : {}, {}'.format(params[0], params[1]))
    return 'answer!'


class ForJungSuTest(unittest.TestCase):
    def test_run(self):
        self.assertEqual(solution([1, 2]), 'answer!')


if __name__ == '__main__':
    testCase = ForJungSuTest('My Test')
    testCase.test_run()
