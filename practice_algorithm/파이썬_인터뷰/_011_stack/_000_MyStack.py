class Node:
    def __init__(self, item, n):
        self.item = item
        self.n = n


class MyStack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.next  # 마지막 다음 노드
        self.last = self.last.next  # 마지막 다음 노드의 참조 변경
        return item
