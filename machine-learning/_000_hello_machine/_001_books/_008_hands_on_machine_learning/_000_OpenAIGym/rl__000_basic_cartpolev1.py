# -*- coding: utf-8 -*-
"""RL/_000_basic_CartPoleV1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1weh8FNVohG7Y6hCFOppoqCoBfMwMokmx
"""

import gym
import random
import numpy as np

env_name = 'CartPole-v1'
env = gym.make(env_name)
print("Observation space: ", env.observation_space)
print("Action space:", env.action_space)

import tensorflow as tf
from tensorflow.keras import layers, models, activations, losses


class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print(f"Action size: {self.action_size}\n")

        self.n_shape = env.observation_space.shape[0]  # 환경의 상태를 가져온다.

    def get_action_hard_coding(self, state):
        # Step 02.
        # action = random.choice(range(self.action_size))
        pole_angle = state[2]
        result = 0 if pole_angle < 0 else 1
        return result


"""# env.reset(): 첫 번째 관측 반환




"""

env.reset()

"""| 인덱스 | 설명 | 의미 |
| --- | :---: | --- | 
| 0 | 카트의 `수평` 위치 | 중앙값 0.0 |
| 1 | 카트의 `속도` | `+`우측, `-`좌측 |
| 2 | 막대의 `각도` | 수직 0.0 |
| 3 | 막대의 `각속도` | `+`시계방향,  `-`반시계방향 |
"""

agent = Agent(env)


def print_result(action_func=None):
    totals = []
    try_range = 500
    for episode in range(try_range):
        episode_rewards = 0
        obs = env.reset()
        for _ in range(200):
            if not action_func:
                # Step 01. gym에서 제공하는 sample 값으로 테스트
                action = env.action_space.sample()
            else:
                # Step 02. hard coding 버전으로 테스트
                action = action_func(obs)

            obs, reward, done, info = env.step(action)
            episode_rewards += reward  # 스텝 이후 reward를 축적한다.

            if done:
                break

        totals.append(episode_rewards)

    print(
        f'****Try score [{try_range}] infomation****\nmean: {np.mean(totals):.3f}\nstd: {np.std(totals):.3f}\nmin: {np.min(totals):.3f}\nmax: {np.max(totals):.3f}')


"""## Step 01. env.action_space.sampe()"""

print_result(None)

"""## Step 02. Hard coding"""

print_result(agent.get_action_hard_coding)

"""# Reinforce(강화하다) algorithm


- `할인 계수(감마)`를 적용한 보상을 모두 합하여 행동을 평가
- 각 행동이 얼마나 좋은지 나쁜지를 추청하는 것 `행동 이익 action advantage`
- 모든 행동의 대가를 (평균을 빼고 표준편차로 나누어) `정규화`해야 한다.
- 위 작업 후  이익의 정이
: `음수`인 행동은 `나쁘고`
: `양수`인 행동은 `좋다`

"""


def ps_model(obs):
    inputs = layers.Input(shape=(obs.shape))
    H = layers.Dense(units=5)(inputs)
    H = layers.Activation('elu')(H)  # exp(feature) - 1 if < 0 else feature
    # H = layers.Activation('relu')(H)  #
    H = layers.Dense(1)(H)
    output = layers.Activation('sigmoid')(H)
    # print(f'output shape : {output.shape}')
    return models.Model(inputs, output)


"""## 한 스텝을 진행할 함수

- 어떤 행동을 하더라도 `옳은` 행동이라고 가정한다.
- 잠시 저장하고 `행동이 옳은지 판명`된 후 조정한다.
---

1. 매 스탭마다 선택된 행동이 더 높은 가능성을 가지도록 만드는 gradient 계산
2. 에피소드를 몇 번 실행한 이후 `각 행동의 이익을 계산`
3. 행동 상태에 따른 처리
  + `양수`일 경우
    *  ***2*** 에서 계산한 `gradient`를 적용,
  + `음수`일 경우
    * ***2***에서 계산한 것과 `반대 gradient`를 적용
    * _미래에 이 행동이 덜 선택되도록_ 반대의 gradient를 적용
  + `연산방법: `각 gradient 벡터와 그에 상응하는 행동의 이익을 곱하면 된다. (**경사 상승법**)
  + `실제 구현: ` **경사 하강법 optimizer**를 사용한다.
4. 모든 결과 gradient 벡터를 `평균` 내어 `경사 하강법 스텝`을 수행한다.


"""


def play_one_step(env, obs, model, loss_fn):
    with tf.GradientTape() as tape:
        # print(obs[np.newaxis])  # 새로운 axis를 생성  #  [[ 0.20046674  0.607944   -0.22266727 -0.61626107]]
        left_proba = model(obs[np.newaxis])
        # print(left_proba)
        l = tf.random.uniform([1, 1])
        # print(l)
        action = (l > left_proba)  # True or False
        # print(action)
        y_target = tf.constant([[1.]]) - tf.cast(action, tf.float32)
        # print(f'y_target :: [{y_target}]')
        loss = tf.reduce_mean(loss_fn(y_target, left_proba))
    grads = tape.gradient(loss, model.trainable_variables)
    obs, reward, done, info = env.step(int(action[0, 0].numpy()))
    return obs, reward, done, grads


"""1. 하나의 관측과 함께 먼저 모델을 호출한다.

?모델은 하나의 배치를 기대하므로 하나의 샘플이 들어 있는 배치가 되도록 관측의 크기를 바꾼다.

- 이 모델은 왼쪽으로 이동할 확률을 출력한다.

2. 0에서 1 사이의 랜덤한 실수를 샘플링 한다. (0-왼쪽, 1-오른쪽)

3. 왼쪽으로 이동할 타깃 확률을 정의한다.
  * 1 빼기 행동
    + 행동이 0(왼쪽)이면 왼쪽으로 이동할 타깃 확률은 1이 됨
    + 행동이 1(오른쪽)이면 타깃 확률이 0이 됨

4. 주어진 손실 함수를 사용해 손실을 계산하고, `테이프`를 사용해 모델의 훈련 가능한 변수에 대한 손실의 `gradient`를 계산한다. <br/> 해당 `gradient`도 적용하기 전 이 행동이 좋은지 나쁜지에 따라 `조정`될 것이다.

5. 선택한 행동을 `플레이`하고 새로운 관측, 보상, 에피소드 종료 여부, `계산한 gradient`를 반환한다.
"""

print(env.reset())
play_one_step(env, env.reset(), ps_model(env.reset()), losses.binary_crossentropy)

"""## Play multiple episodes

"""


def play_multiple_episodes(env, n_episodes, n_max_steps, model, loss_fn):
    all_rewards = []  # 한 에피소드의 합산 리워드
    all_grads = []  # 한 에피소드의 gradient 모음

    for episode in range(n_episodes):
        """에피소드 반복"""
        current_rewards = []
        current_grads = []
        obs = env.reset()
        for step in range(n_max_steps):
            """step 반복"""
            obs, reward, done, grads = play_one_step(env, obs, model, loss_fn)
            current_rewards.append(reward)
            current_grads.append(grads)
            if done:
                break
        print(f'current reward: {np.sum(current_rewards)}')
        all_rewards.append(current_rewards)
        all_grads.append(current_grads)

    # print('-'*100)
    # print(all_grads)
    return all_rewards, all_grads


"""### `각 스텝`에서 할인된 `미래 보상의 합`: discount_rewards


"""


def discount_rewards(rewards, discount_factor):
    discounted = np.array(rewards)
    for step in range(len(rewards) - 2, -1, -1):
        # print(discounted)
        # result:
        # [  10    0 -100] : input
        # [  10  -80 -100]
        # array([ -54,  -80, -100]) : output
        discounted[step] += discounted[step + 1] * discount_factor

    return discounted


"""### `여러 에피소드`에 걸쳐 할인 + 계산된 `모든 보상(대가)`에서 ***`평균`을 빼고 `표준편차를 나누어` 정규화***

"""


def discount_and_normalize_rewards(all_rewards, discount_factor):
    all_discounted_rewards = [discount_rewards(rewards, discount_factor) \
                              for rewards in all_rewards]
    flat_rewards = np.concatenate(all_discounted_rewards)
    # print(flat_rewards.shape)
    reward_mean = flat_rewards.mean()
    reward_std = flat_rewards.std()
    print(f'mean: {reward_mean}, std: {reward_std}')
    return [(discounted_rewards - reward_mean) / reward_std \
            for discounted_rewards in all_discounted_rewards]


"""#### discount 함수 동작 확인하기"""

discount_rewards([10, 0, -100], discount_factor=.8)

discount_and_normalize_rewards([[10, 0, -50], [10, 20]], discount_factor=.8)

"""**두 에피소드의 정규화된 행동 이익**

- 첫 번째 에피소드는 두 번째에 비해 너무 나쁘므로 `정규화된 이익이 모두 음수`

- 두 번째 에피소드의 행동은 `모두 좋은 것으로 간주`

---

### `하이퍼 파라미터 정의` & `훈련 반복`


- 반복 **150번 실행**
- 각 반복은 `에피소드 10개`를 진행
- 각 에피소드는 `스텝`을 `최대 200번` 플레이
- `할인 계수`는 0.95 적용
"""

n_iteration = 150
n_episodes_per_update = 10
n_max_steps = 200
discount_factor = 0.95

# 일반적인 학습률인 0.01을 사용
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
loss_fn = losses.binary_crossentropy

model = ps_model(np.array([1, 2, 3, 4]))

"""## 훈련 반복 실행 :: Run"""

for iteration in range(n_iteration):
    all_rewards, all_grads = play_multiple_episodes(
        env, n_episodes_per_update, n_max_steps, model, loss_fn
    )

    all_final_rewards = discount_and_normalize_rewards(
        all_rewards, discount_factor=discount_factor
    )

    all_mean_grads = []
    # print(model.trainable_variables)
    for var_index in range(len(model.trainable_variables)):
        mean_grads = tf.reduce_mean([final_reward * all_grads[episode_index][step][var_index] \
                                     for episode_index, final_rewards in enumerate(all_final_rewards) \
                                     for step, final_reward in enumerate(final_rewards)], axis=0)
        all_mean_grads.append(mean_grads)

    optimizer.apply_gradients(zip(all_mean_grads, model.trainable_variables))

"""1. 10번 플레이하고 `각 에피소드`와 `스텝`에 대한 `모든 보상`과 `gradient`를 반환한다.
2. 각 행동의 정규화된 이익인 `final_reward`를 계산하고, 각 행동이 좋은지 나쁜지를 알려준다.
3. `모든 에피소드`와 `모든 스텝`에 대한 각 변수의 `gradient`를 `final_reward`로 가중치를 반영하여 `평균`을 낸다.
4. `평균`한 `gradient`를 `optimizer`에 적용한다.
"""

print(model.weights)