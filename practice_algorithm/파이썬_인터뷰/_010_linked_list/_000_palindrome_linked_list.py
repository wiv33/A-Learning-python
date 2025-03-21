class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_the_linked_list(head: ListNode) -> bool:
    q: [] = []
    if not head:
        return True

    node = head

    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


result = is_palindrome_the_linked_list(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
assert result

res = is_palindrome_the_linked_list(ListNode(1, ListNode(2)))
assert not res


def is_palindrome_deque_v(head: ListNode) -> bool:
    from collections import deque
    deq = deque()

    if not head:
        return True

    while head:
        deq.append(head.val)
        head = head.next

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False

    return True


res = is_palindrome_deque_v(ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(1)))))))
assert res
