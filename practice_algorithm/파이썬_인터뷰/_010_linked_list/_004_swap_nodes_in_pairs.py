class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next_node = next_node


def swap_pairs(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next_node:
        cur.val, cur.next_node.val = cur.next_node.val, cur.val

        cur = cur.next_node.next_node

    return head


result = swap_pairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

while result:
    print(result.val)
    result = result.next_node
