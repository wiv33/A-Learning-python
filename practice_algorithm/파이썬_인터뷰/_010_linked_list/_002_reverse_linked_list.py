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
# input 1 -> 2 -> 3 -> 4 -> 5
# res   5 -> 4 -> 3 -> 2 -> 1
while res:
    print(res.val)
    res = res.next

print("=== end ===")


def reverse_linked_list_other(head: ListNode) -> ListNode:
    def reverse_node(node: ListNode, prev: ListNode = None) -> ListNode:
        if not node:
            return prev

        next_node, node.next = node.next, prev
        return reverse_node(next_node, node)

    return reverse_node(head)


res = reverse_linked_list_other(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
while res:
    print(res.val)
    res = res.next


print("== start for ==")


def reverse_linked_list_for(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next_node, node.next = node.next, prev
        prev, node = node, next_node

    return prev


res = reverse_linked_list_for(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
while res:
    print(res.val)
    res = res.next
