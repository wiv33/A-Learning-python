import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.first_input = "abcabcbb"

    def test_final(self):
        pass
        # actual = Solution().lengthOfLongestSubstring("abcabcbb")
        # expected = 3
        # self.assertEqual(expected, actual)
        #
        # actual = Solution().lengthOfLongestSubstring("bbbbb")
        # expected = 1
        # self.assertEqual(expected, 1)
        #
        # actual = Solution().lengthOfLongestSubstring("pwwkew")
        # expected = 3
        # self.assertEqual(expected, 3)

    # 덩어리로 확인할 수 없으니 문자열을 쪼개야 한다.
    # python은 문자열을 이미 배열로 가지고 있다.
    # dict와 다른 점 테스트
    def test_access_string_index_key(self):
        # input_data index 키에 원소를 넣을 수 없다.
        with self.assertRaises(TypeError):
            print('a' == self.first_input['a'])

    # integer 값을 넣어서 가져온다.
    def test_access_string_index(self):
        self.assertEqual('a', self.first_input[0])
        self.assertEqual('a', self.first_input[3])
        self.assertEqual('b', self.first_input[4])

    def test_get_first_pattern(self):
        actual = get_first_pattern(self.first_input)
        expected = ('abc', 3)
        self.assertEqual(expected[1], actual)

    def test_bbbbbbb(self):
        actual2 = get_first_pattern('bbbbbbb')
        expected2 = ('b', 1)
        self.assertEqual(expected2[1], actual2)

    def test_pwwkew(self):
        actual3 = get_first_pattern("pwwkew")
        expected3 = ('wke', 3)
        self.assertEqual(expected3[1], actual3)

    def test_aab(self):
        actual = get_first_pattern("aab")
        expected = ('ab', 2)
        self.assertEqual(expected[1], actual)

    def test_bdb(self):
        actual = get_first_pattern("bdb")
        expected = ('bd', 2)
        self.assertEqual(expected[1], actual)

    def test_empty_input(self):
        self.assertEqual(0, get_first_pattern(""))

    def test_high_pass(self):
        actual = get_first_pattern("brnk")
        expected = 4
        self.assertEqual(expected, actual)

        actual3 = get_first_pattern("au")
        expected3 = ('au', 2)
        self.assertEqual(expected3[1], actual3)

    def test_cdd(self):
        actual = get_first_pattern("cdd")
        expected = 2
        self.assertEqual(expected, actual)

    def test_aaca(self):
        actual = get_first_pattern("aaca")
        expected = 2
        self.assertEqual(expected, actual)

    def test_abcb(self):
        actual = get_first_pattern("abcb")
        expected = 3
        self.assertEqual(expected, actual)

    def test_dvdf(self):
        actual = get_first_pattern("dvdf")
        expected = 3
        self.assertEqual(expected, actual)


def get_first_pattern(s: str) -> int:
    length = len(s)

    if length == 0:
        return 0

    acc = s[0] or ""
    if is_high_pass_not_match(length, s):
        return length

    for i in range(length - 1):
        l1, l2 = s[i], s[i + 1]

        if acc.__contains__(l2) and acc.find(l2) > 0:
            acc = acc[acc.find(l2):]
            print(acc)

        if acc[0] == l2:
            if is_answer_remove_duplication(acc, i, s):
                return len(acc)

        if l1 == l2:
            if not_exists_next(i, s):
                return len(acc)
            acc = ""

        acc += l2

    return len(acc)


def not_exists_next(i, s):
    return (i + 2) == len(s)


def is_answer_remove_duplication(acc, i, s):
    print("is_answer param {}".format(acc))
    split = s[i + 1:].split(acc)
    for x in split:
        if x:
            return False
    print(split)
    return i > 0 and len(acc) > len(split[len(split) - 1])


def is_high_pass_not_match(length, s):
    for z in range(1, length):
        if s[z - 1] == s[z]:
            return False


if __name__ == '__main__':
    unittest.main()
