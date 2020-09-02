import unittest

from .second_solution import ListNode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.l1 = ListNode(2, ListNode(4, ListNode(3)))
        self.l2 = ListNode(5, ListNode(6, ListNode(4)))

    def test_import(self):
        self.assertIsNotNone(self.l1)
        self.assertIsNotNone(self.l2)
        self.assertEqual(2, self.l1.val, "l1.val is 2")
        self.assertEqual(5, self.l2.val, "l2.val is 5")
        self.assertEqual(4, self.l1.next.val, "l1.next.val is 4")
        self.assertEqual(6, self.l2.next.val, "l2.next.val is 6")
        self.assertEqual(3, self.l1.next.next.val, "l1.next.next.val is 3")
        self.assertEqual(4, self.l2.next.next.val, "l2.next.next.val is 4")

    def tearDown(self) -> None:
        self.l1, self.l2, self.expected = None, None, None

    def test_calculate(self):
        self.assertEqual(7, self.l1.val + self.l2.val, "expected 7, actual 7")
        d, m = divmod(10, 10)
        self.assertEqual(d, 1, "div is 1")
        self.assertEqual(m, 0, "mod is 0")

    def test_node_chain(self):
        pass


if __name__ == '__main__':
    unittest.main()
