# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(-3333)
        root.next = head

        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next


if __name__ == '__main__':
    result = Solution().reverseBetween(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 2, 5)

    for expected in [1, 5, 4, 3, 2, 6]:
        assert expected == result.val
        result = result.next
