class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_runner(head: ListNode) -> bool:
    rev = None  #
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        # 오른쪽의 값 기준, 왼쪽 차례대로 대입 됨.
        # 만약 처음 slow가 None이 되면 오류가 발생할 로직
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


result = is_palindrome_runner(ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(1)))))))
assert result
