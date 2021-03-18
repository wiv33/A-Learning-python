# https://leetcode.com/problems/implement-stack-using-queues/

# 큐를 이용해 다음 연산을 지원하는 스택을 구현
# push(x): 요소 x를 스택에 삽입
# pop(): 스택의 첫 번재 요소를 삭제
# top(): 스택의 첫 번째 요소를 가져옴
# is_empty(): 스택이 비어 있는지 여부를 반환

import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        # api 활용
<<<<<<< HEAD
        # self.q.appendleft(x)
        # 직접 구현
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def top(self):
        return self.q.pop()
=======
        self.q.appendleft(x)
        # 직접 구현
        # self.q.append(x)
        # for _ in range(len(self.q) - 1):
        #     self.q.append(self.q.popleft())

    def top(self):
        return self.q[0]
>>>>>>> refs/remotes/origin/master

    def pop(self):
        return self.q.popleft()

    def is_empty(self):
        return len(self.q) == 0


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)

<<<<<<< HEAD
    assert s.top() == 1
    assert s.pop() == 2
=======
    assert s.pop() == 2
    assert s.pop() == 1
>>>>>>> refs/remotes/origin/master

    assert s.is_empty()
