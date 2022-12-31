class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node


def odd_even_list_node(head: ListNode):
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


if __name__ == '__main__':
    param = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    actual = odd_even_list_node(param)

    expected = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))

    assert expected.val == actual.val
    expected, actual = expected.next, actual.next
    assert expected.val == actual.val
    expected, actual = expected.next, actual.next
    assert expected.val == actual.val
    expected, actual = expected.next, actual.next
    assert expected.val == actual.val
    expected, actual = expected.next, actual.next
    assert expected.val == actual.val
