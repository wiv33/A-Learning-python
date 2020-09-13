class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node


def odd_even_list_node(head: ListNode):
    return ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))


param = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
actual = odd_even_list_node(param)

expected = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))

assert expected.val == actual.val
expected, actual = expected.next, actual.next
assert expected.val == 3
expected, actual = expected.next, actual.next
assert expected.val == 5
expected, actual = expected.next, actual.next
assert expected.val == 2
expected, actual = expected.next, actual.next
assert expected.val == 4
