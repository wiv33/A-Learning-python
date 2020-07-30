# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


def generate_node(arr: list):
    result = ""
    for v in arr:
        result += "ListNode({},".format(v)
    result += (")" * len(arr))
    return result
