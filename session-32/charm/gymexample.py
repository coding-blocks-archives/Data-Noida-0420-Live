import gym
import numpy as np
import time
env = gym.make('CartPole-v0')
env.reset()
env.unwrapped.length = .5
for _ in range(1000):
    env.render()

    if(env.state[0] > 0):
        env.step(0)
    else:
        env.step(1)


env.close()