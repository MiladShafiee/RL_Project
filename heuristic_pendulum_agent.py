import gymnasium as gym
import numpy as np

class HeuristicPendulumAgent:
    def __init__(self, env):
        self.state_size = env.observation_space.shape[0]
        self.action_size = env.action_space.shape[0]
        
    def compute_action(self, state):
        if (state[0]<=0): 
            # if the pendulum is lower side of the page, apply a constant torque with the same sign of the angular velocity
            action = np.sign(state[2])*0.8
        else:
            # if the pendulum is upper side of the page, apply a constant torque with the negative sign of the angular velocity
            action = np.sign(state[2])*-0.8
        
        return  action
