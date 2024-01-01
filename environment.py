import functools
import random
import numpy as np
from copy import copy
from gymnasium.spaces import Discrete, MultiDiscrete
from parsing import parse_environment

from pettingzoo import ParallelEnv


class CustomEnvironment(ParallelEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self, filename):
        
        self.filename = filename
        
        self.gridworld = None
        
        self.robot_pos = None
        self.robot_goals = None
        
        self.possible_agents = parse_environment(self.filename)[1].keys
        
        self.timestep = None

    def reset(self, seed=None, options=None):
        self.agents = copy(self.possible_agents)
        self.timestep = 0
        self.gridworld, self.robot_pos, self.robot_goals = parse_environment(self.filename)
        
        observations = {
            a: tuple(robot[0] + len(self.gridworld) * robot[1] for robot in self.robot_pos) + tuple(goal[0] + len(self.gridworld) * goal[1] for goal in self.robot_goals)
            for a in self.agents
        }
        
        # Get dummy infos. Necessary for proper parallel_to_aec conversion
        
        infos = {a: {} for a in self.agents}
        
        return observations, infos

    def step(self, actions):
        for agent in self.agents:
            agent_action = actions[agent]

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]