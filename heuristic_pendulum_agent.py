import gymnasium as gym
import numpy as np

class HeuristicPendulumAgent:
    def __init__(self, env):
        self.state_size = env.observation_space.shape[0]
        self.action_size = env.action_space.shape[0]
        
    def compute_action(self, state):
        print(state)
        if (state[0]<=0):
            action = np.sign(state[2])*0.8
        else:
            action = np.sign(state[2])*-0.8
        
        return  action
