import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.first_input = "abcabcbb"

    def test_final(self):
        actual = Solution().lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(expected, actual)

        actual = Solution().lengthOfLongestSubstring("bbbbb")
        expected = 1
        self.assertEqual(expected, 1)

        actual = Solution().lengthOfLongestSubstring("pwwkew")
        expected = 3
        self.assertEqual(expected, 3)

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


if __name__ == '__main__':
    unittest.main()
