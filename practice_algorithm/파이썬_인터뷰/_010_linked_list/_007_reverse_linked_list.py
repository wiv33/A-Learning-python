from _006_merge_two_sorted_lists import ListNode


# https://leetcode.com/problems/reverse-linked-list/
#

# input: 1->2->3->4->5->null
# output: 5->4->3->2->1->null

def reverse_list(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev

        n, node.next = node.next, prev
        return reverse(n, node)

    return reverse(head)


def reverse_list_assert(func):
    actual = func(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))

    while actual:
        assert expected.val == actual.val
        actual, expected = actual.next, expected.next


def reverse_list_forloop(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        n, node.next = node.next, prev
        prev, node = node, n

    return prev


if __name__ == '__main__':
    reverse_list_assert(reverse_list)
    reverse_list_assert(reverse_list_forloop)
