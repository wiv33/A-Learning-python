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


def swap_pairs_loop(head: ListNode) -> ListNode:
    root = prev = ListNode()
    prev.next_node = head

    while head and head.next_node:
        # b가 head를 가리키도록 할당
        b = head.next_node
        head.next_node = b.next_node
        b.next_node = head

        # prev가 b를 가리키도록 할당
        prev.next_node = b

        # 다음 비교를 위해 이동
        head = head.next_node
        prev = prev.next_node.next_node
    return root.next_node


print("next step")
result = swap_pairs_loop(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

while result:
    print(result.val)
    result = result.next_node


def swap_pairs_recursive(head: ListNode) -> ListNode:
    if head and head.next_node:
        p = head.next_node

        # 스왑된 값을 반환 받음
        head.next_node = swap_pairs_recursive(p.next_node)
        p.next_node = head
        return p

    return head


print("next step")

result = swap_pairs_recursive(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

while result:
    print(result.val)
    result = result.next_node
