from practice_algorithm.파이썬_인터뷰._010_linked_list.LinkedNode import ListNode


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def swap_pairs_val(self):
        cur = self.head

        while cur:
            cur.val, cur.next_node.val = cur.next_node.val, cur.val
            cur = cur.next_node.next_node

        return self.head

    def swap_pairs_node(self):
        # https://www.figma.com/file/zwgIYjBbDm7drOB9c7G19i/swap_pairs_node?node-id=682%3A4066&t=KkOWbobDVY6Cd9qA-1
        root = prev = ListNode(-1)
        prev.next_node = self.head

        while self.head and self.head.next_node:
            b = self.head.next_node
            self.head.next_node = b.next_node
            b.next_node = self.head

            prev.next_node = b

            self.head = self.head.next_node  # 7
            prev = prev.next_node.next_node

        return root.next_node

    def swap_pairs_recursive(self):
        return self._swap_pairs_recursive(self.head)

    def _swap_pairs_recursive(self, head):
        if head and head.next_node:
            p = head.next_node
            # 스왑된 값을 반환 받음
            head.next_node = self._swap_pairs_recursive(p.next_node)
            p.next_node = head
            return p

        return head


if __name__ == '__main__':
    result_head = Solution(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).swap_pairs_recursive()

    while result_head:
        print(result_head.val)
        result_head = result_head.next_node
