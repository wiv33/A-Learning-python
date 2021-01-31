from _005_odd_even_linked_list import ListNode


# https://leetcode.com/problems/merge-two-sorted-lists

# input: 1->2->4, 1->3->4
# output: 1->1->2->3->4->4

# 정렬되어 있는 두 연결 리스트를 합치기


def merge_two_lists_recursive(l1, l2) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = merge_two_lists_recursive(l1.next, l2)
    return l1


