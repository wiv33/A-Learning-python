import gym

env = gym.make('CartPole-v1')
obs = env.reset()

print(obs)

img = env.render(mode='rgb_array')
print(img.shape)

action = 10
obs, reward, done, info, = env.step(action)
print(obs)

env.close()