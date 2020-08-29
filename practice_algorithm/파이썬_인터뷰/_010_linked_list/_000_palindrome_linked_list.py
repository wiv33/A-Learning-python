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

import collections


def is_palindrome_deque_v(head: ListNode) -> bool:
    if not head:
        return True

    deque: [] = collections.deque()
    node = head

    while node:
        deque.append(node.val)
        node = node.next

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False

    return True


res = is_palindrome_deque_v(ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(1)))))))
assert res
