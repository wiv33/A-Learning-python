import unittest

from second_solution import ListNode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.l1 = ListNode(2, ListNode(4, ListNode(3)))
        self.l2 = ListNode(5, ListNode(6, ListNode(4)))

    def test_import(self):
        self.assertIsNotNone(self.l1)
        self.assertIsNotNone(self.l2)
        self.assertEqual(self.l1.val, 2, "l1.val is 2")
        self.assertEqual(self.l2.val, 5, "l2.val is 5")
        self.assertEqual(self.l1.next.val, 4, "l1.next.val is 4")
        self.assertEqual(self.l2.next.val, 6, "l2.next.val is 6")
        self.assertEqual(self.l1.next.next.val, 3, "l1.next.next.val is 3")
        self.assertEqual(self.l2.next.next.val, 4, "l2.next.next.val is 4")


if __name__ == '__main__':
    unittest.main()
