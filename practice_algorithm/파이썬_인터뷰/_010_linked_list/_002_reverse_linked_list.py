class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val: int = val
        self.next: ListNode = next_node


def reverse_linked_list(head: ListNode, prev: ListNode = None) -> ListNode:
    if not head:
        return prev

    next_node, head.next = head.next, prev
    return reverse_linked_list(next_node, head)


res = reverse_linked_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

while res:
    print(res.val)
    res = res.next
