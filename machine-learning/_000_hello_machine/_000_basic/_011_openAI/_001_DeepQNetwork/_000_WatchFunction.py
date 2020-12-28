import gym
import random
import numpy as np
import tensorflow as tf
import time

import sys
import os


# tag::class[]
class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n
        print(f'취할 수 있는 행동의 최대 수: {self.action_size}')

    def get_action(self):
        act = random.choice(range(self.action_size))
        print(f'선택한 행동: {act}')
        return act

# end::class[]

print(f'Gym: {gym.__version__}')
print(f'Tensorflow: {tf.__version__}')

env_name = 'CartPole-v1'
env = gym.make(env_name)

print(f'Observation space: {env.observation_space}')
print(f'Action space: {env.action_space}')

agent = Agent(env)
state = env.reset()


for _ in range(200):
    action = agent.get_action()
    obs, reward, done, info = env.step(action)
    env.render()
    time.sleep(1)
    print("-" * 10)
    print(f'is done: {done}\n관측값: {obs}\nreward: {reward}\ninfo: {info}')
    print("-" * 10)

env.close()
