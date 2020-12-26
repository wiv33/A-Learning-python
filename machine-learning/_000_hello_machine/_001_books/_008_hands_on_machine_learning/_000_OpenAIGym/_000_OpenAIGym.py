import gym
import numpy as np

env = gym.make('CartPole-v1')
obs = env.reset()

print(obs)

img = env.render(mode='rgb_array')
print(img.shape)

action = 1
obs, reward, done, info, = env.step(action)
print(obs)


def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1


totals = []

for episode in range(300):
    episode_rewards = []
    obs = env.reset()
    for step in range(200):
        action = basic_policy(obs)
        obs, reward, done, info = env.step(action)
        episode_rewards.append(reward)
        if done:
            break

    totals.append(np.sum(episode_rewards))

print(f'** result info **\n'
      f'mean: {np.mean(totals)}\n'
      f'std: {np.std(totals)}\n'
      f'min: {np.mean(totals)}\n'
      f'max: {np.max(totals)}')
