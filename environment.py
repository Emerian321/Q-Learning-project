import functools
import random
import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete

from pettingzoo import ParallelEnv


class CustomEnvironment(ParallelEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self, gridworld, robots, goals):
        
        self.gridwolrd = gridworld
        
        self.robot_pos = {"robot" + str(i+1): robots[i] for i in range(len(robots))}
        self.robot_goals = {"robot" + str(i+1): goals[i] for i in range(len(goals))}
        
        self.possible_agents = ["robot" + str(i+1) for i in range(len(robots))]

    def reset(self, seed=None, options=None):
        pass

    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]