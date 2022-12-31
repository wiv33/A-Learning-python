class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next_node = next_node


def reverse_node(head: ListNode, prev_node: ListNode = None) -> ListNode:
    while head:
        node, head.next_node = head.next_node, prev_node
        prev_node, head = head, node

    return prev_node


class Solution:
    def __init__(self, first: ListNode, second: ListNode):
        self.first = first
        self.second = second

    def add_two_sum(self):
        reverse_first = reverse_node(self.first)
        reverse_second = reverse_node(self.second)
        first_list = self.to_list(reverse_first)
        second_list = self.to_list(reverse_second)

        result: ListNode = None
        for x in str(self.list_to_int(first_list) + self.list_to_int(second_list)):
            node = ListNode(x)
            node.next_node = result

        return node

    def list_to_int(self, target_list: []) -> int:
        return int(''.join(str(s) for s in target_list))

    def to_list(self, node: ListNode) -> []:
        result = []
        while node:
            result.append(node.val)
            node = node.next_node
        return result


solution = Solution(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
print(solution.add_two_sum().val)
