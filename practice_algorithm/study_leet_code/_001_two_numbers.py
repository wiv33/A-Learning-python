# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        arr = []
        temp1, temp2 = l1, l2
        n_val = 0
        while l1 is not None or l2 is not None or n_val is not 0:
            a, b = 0, 0
            if hasattr(l1, "val"):
                a = l1.val
            if hasattr(l2, "val"):
                b = l2.val

            if hasattr(l1, "next"):
                l1 = l1.next
            if hasattr(l2, "next"):
                l2 = l2.next

            # 현재 값
            v = a + b + n_val
            # 몫이 있으면 n + 1 요소는 증가, n은 v/10 + m
            d, m = divmod(v, 10)
            print(d, m)
            if d > 0:
                arr.append(m)
                if 0 >= n_val:
                    n_val = 1
                else:
                    n_val = 0
            else:
                print('v = {}'.format(v))
                arr.append(v)
                n_val = 0

            # v + d >= 10: n + 1 요소에 1을 증가시킨다.
            v + d

        return eval(generate_node(arr))


def generate_node(arr: list):
    result = ""
    for v in arr:
        result += "ListNode({},".format(v)
    result += (")" * len(arr))
    return result
