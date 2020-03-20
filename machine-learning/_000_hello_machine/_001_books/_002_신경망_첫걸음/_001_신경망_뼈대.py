"""
- 초기화: 입력, 은닉, 출력 노드의 수 설정
- 학습: 학습 데이터들을 통해 학습하고 이에 따라 가중치를 업데이트
- 질의: 입력을 받아 연산한 후 출력 노드에서 답을 전달

"""

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rage):
        # 입력, 은닉, 출력 계층의 노드
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # 학습률
        self.lr=learning_rage
        pass

    def train(self):
        pass

    def query(self):
        pass