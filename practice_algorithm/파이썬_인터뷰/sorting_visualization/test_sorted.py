import unittest


class MyTestCase(unittest.TestCase):
    def test_number_sorted(self):
        a = [2, 5, 1, 9, 7]
        actual = sorted(a)
        self.assertEqual([1, 2, 5, 7, 9], actual)

    def test_str_sorted(self):
        a = 'zdcja'
        actual = sorted(a)
        self.assertEqual(['a', 'c', 'd', 'j', 'z'], actual)

        join = "".join(actual)
        self.assertEqual('acdjz', join)

    def test_list_sort(self):
        actual = [5, 8, 2, 6]
        actual.sort()
        self.assertEqual([2, 5, 6, 8], actual)

    def test_sort_by_len(self):
        data = ['zzzz', 'jjj', 'rr', 'aaaaa']
        actual = sorted(data, key=len)
        self.assertEqual(['rr', 'jjj', 'zzzz', 'aaaaa'], actual)

    def test_sort_by_user_custom_key(self):
        def fn(s):
            return s[0], s[2]

        data = ['cdc', 'aza', 'caz']
        actual = sorted(data, key=fn)
        # actual = sorted(data, key=lambda x: (x[0], x[-1]))

        self.assertEqual(['aza', 'cdc', 'caz'], actual)


if __name__ == '__main__':
    unittest.main()
