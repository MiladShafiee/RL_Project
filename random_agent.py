import gymnasium as gym
import numpy as np

class RandomAgent:
    def __init__(self, env):
        self.state_size = env.observation_space.shape[0]
        self.action_size = env.action_space.shape[0]
        
    def compute_action(self, state):
        return np.random.uniform(-1, 1, size=(self.action_size, ))
