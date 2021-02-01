from _005_odd_even_linked_list import ListNode


# https://leetcode.com/problems/merge-two-sorted-lists

# input: 1->2->4, 1->3->4
# output: 1->1->2->3->4->4

# 정렬되어 있는 두 연결 리스트를 합치기


def merge_two_lists_recursive(l1, l2) -> ListNode:
    # 우선순위
    # 1. l1.val > l2.val
    # 2. l2 and
    # 3. not l1
    # 4. or
    if (not l1) or (l2 and l1.val > l2.val):
        # l1이 l2보다 크면 스왑
        l1, l2 = l2, l1

    if l1:
        # li.next를 통해 재귀
        l1.next = merge_two_lists_recursive(l1.next, l2)

    return l1


if __name__ == '__main__':
    param_l1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(7)))))
    param_l2 = ListNode(2, ListNode(3, ListNode(7, ListNode(7, ListNode(9)))))
    result = merge_two_lists_recursive(param_l1, param_l2)
    expected = ListNode(1,
                ListNode(1,
                 ListNode(2,
                  ListNode(2,
                   ListNode(3,
                    ListNode(3,
                     ListNode(7,
                      ListNode(7,
                       ListNode(7,
                        ListNode(9))))))))))

    while result or expected:
        assert result.val == expected.val
        result, expected = result.next, expected.next
