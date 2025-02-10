# Raghav Sriram
# Chapter 18

import numpy as np
import tensorflow as tf

from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.trajectories import time_step as ts
from tf_agents.specs import array_spec
from tf_agents.environments import py_environment

class SimpleEnvironment(py_environment.PyEnvironment):

    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(2,), dtype=np.float32, minimum=0, maximum=10, name='observation')
        self._state = 0
        self._episode_ended = False

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._state = 0
        self._episode_ended = False
        return ts.restart(np.array([0, 0], dtype=np.float32))

    def _step(self, action):
        if self._episode_ended:
            return self.reset()

        if action == 1:
            self._state += 1
        else:
            self._state -= 1

        if self._state > 9:
            self._episode_ended = True
            return ts.termination(np.array([self._state, self._state], dtype=np.float32), 1)
        elif self._state < 0:
            self._episode_ended = True
            return ts.termination(np.array([self._state, self._state], dtype=np.float32), 0)
        else:
            return ts.transition(np.array([self._state, self._state], dtype=np.float32), reward=0)

tf_env.reset()
for _ in range(10):
    action = np.random.randint(0, 2)
    time_step = tf_env.step(action)
    print('Step:', time_step)

env = suite_gym.load('CartPole-v0')
tf_env = tf_py_environment.TFPyEnvironment(env)

time_step = tf_env.reset()
rewards = []
steps = []
num_episodes = 5

for _ in range(num_episodes):
  episode_reward = 0
  episode_steps = 0
  while not time_step.is_last():
    action = tf.random.uniform([1], 0, 2, dtype=tf.int32)
    time_step = tf_env.step(action)
    episode_steps += 1
    episode_reward += time_step.reward.numpy()
  rewards.append(episode_reward)
  steps.append(episode_steps)
  time_step = tf_env.reset()

num_steps = np.sum(steps)
avg_length = np.mean(steps)
avg_reward = np.mean(rewards)

print('num_episodes:', num_episodes, 'num_steps:', num_steps)
print('avg_length', avg_length, 'avg_reward:', avg_reward)