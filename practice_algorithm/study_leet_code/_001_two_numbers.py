# https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        val_arr = []
        temp1, temp2 = l1, l2
        # first_l2 = l2
        increment = 0
        unbal: bool = False

        while l1 is not None or l2 is not None:
            if unbal and len(val_arr) == 1:
                if l1 is None:
                    return temp2
                elif l2 is None:
                    return temp1

            a, b = 0, 0
            if hasattr(l1, "val"):
                a = l1.val
            if hasattr(l2, "val"):
                b = l2.val

            v = a + b
            d, m = divmod(v, 10)
            if d > 0:
                v = v - v + m
                increment = d
            elif increment > 0:
                v += increment
                increment = 0

            val_arr.append(v)
            if increment is not 0 and l2.next is None:
                val_arr.append(d)

            l1 = l1.next
            l2 = l2.next

            if l1 is None or l2 is None:
                unbal = True

        return eval(generate_node(val_arr))


def generate_node(arr: list):
    result = ""
    for v in arr:
        result += "ListNode({},".format(v)
    result += (")" * len(arr))
    return result
