from unittest import TestCase

from linear_search import search_list, search_arr, search_name


class TestSearchList(TestCase):
    def test_search_list(self):
        arr = [12, 22, 33, 55]
        self.assertEqual(2, search_list(arr, 33))
        self.assertEqual(3, search_list(arr, 55))
        self.assertEqual(-1, search_list(arr, 77))

    def test_search_result_arr(self):
        arr = [12, 22, 33, 55, 33, 77, 55, 77, 66]
        expected = [3, 6]
        self.assertEqual(expected, search_arr(arr, 55))

    def test_search_names(self):
        stu_no = [35, 14, 67, 105]
        stu_name = ["Justin", "John", "Mike", "Summer"]
        search_num = 67
        expected = "Mike"

        self.assertEqual(expected, search_name(stu_no, stu_name, search_num))
        self.assertEqual("?", search_name(stu_no, stu_name, 37))
