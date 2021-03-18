# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        # 재입력이란?
        # input의 값을 output으로 옮기는 작업
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def is_empty(self):
        return self.input == [] and self.output == []


