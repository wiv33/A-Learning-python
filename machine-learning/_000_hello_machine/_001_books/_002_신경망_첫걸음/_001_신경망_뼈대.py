"""
- 초기화: 입력, 은닉, 출력 노드의 수 설정
- 학습: 학습 데이터들을 통해 학습하고 이에 따라 가중치를 업데이트
- 질의: 입력을 받아 연산한 후 출력 노드에서 답을 전달

"""
import numpy as np
import scipy.special


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rage):
        # 입력, 은닉, 출력 계층의 노드
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # 학습률
        self.lr = learning_rage

        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 활성화 함수로 시그모이드 함수를 이용
        self.activation_func = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        # 입력 리스트를 2차원의 행렬로 반환
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = np.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호 계산
        hidden_outputs = self.activation_func(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = np.dot(self.who, hidden_outputs)

        final_outputs = self.activation_func(final_inputs)
        pass

    # 입력을 받아 출력을 반환한다.
    # X = W * I
    # hidden = input_hidden * I
    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호 계산
        hidden_inputs = np.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호 계산
        hidden_outputs = self.activation_func(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = np.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_func(final_inputs)
        return final_outputs


input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# 학습률은 0.3으로 정의
learning_rate = 0.3

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes=output_nodes, learning_rage=learning_rate)
