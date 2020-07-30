# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        초기값 설정
        :current
            현재 값을 loop에서 새로운 노드로 갱신하고 연결한다.
        :result
            반환 값
        """
        current = result = ListNode(0)

        # 현재 값에서 10 이상이면 다음 노드에 1이 추가된다
        increment = 0

        # 세 개 중 한 값이라도 있다면 계속 노드를 연결한다.
        while l1 or l2 or increment:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            #
            total = a + b + increment
            increment, m = divmod(total, 10)

            current.next = ListNode(m)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
