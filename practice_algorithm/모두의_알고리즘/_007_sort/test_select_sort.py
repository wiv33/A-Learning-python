from unittest import TestCase

from select_sort import PsSort


class TestPsSort(TestCase):
    def test_sel_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], PsSort([3, 4, 2, 1, 5]).sel_sort())

