# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        increment = 0

        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        val = a + b + increment
        increment, m = divmod(val, 10)

        first = ListNode(m)
        l1 = l1.next if hasattr(l1, "next") else None
        l2 = l2.next if hasattr(l2, "next") else None
        while l1 or l2 or increment:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            val = a + b + increment
            increment, m = divmod(val, 10)

            first.next = ListNode(m)

            l1 = l1.next if hasattr(l1, "next") else None
            l2 = l2.next if hasattr(l2, "next") else None

        if increment > 0:
            first.next = ListNode(increment)

        return first

