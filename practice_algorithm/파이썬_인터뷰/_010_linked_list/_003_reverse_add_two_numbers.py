import functools

res = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
print(res)
string = ''.join(map(str, [1, 2, 3, 4, 5]))
print(string)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        my_sum = 0
        if l1:
            my_sum += l1.val
            l1 = l1.next
        if l2:
            my_sum += l2.val
            l2 = l2.next

        carry, val = divmod(my_sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


if __name__ == '__main__':

    result = add_two_numbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))

    while result:
        print(result.val)
        result = result.next
