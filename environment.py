import functools
import random
import numpy as np
from copy import deepcopy, copy
from gymnasium.spaces import Discrete, MultiDiscrete
from parsing import parse_environment

from pettingzoo import ParallelEnv


class Environment(ParallelEnv):
    metadata = {
        "name": "Cooperative Seeker",
    }

    def __init__(self, filename):
        
        self.filename = filename
        self.agents = None
        
        self.gridworld = None
        
        self.robot_pos = None
        self.robot_goals = None
        
        self.possible_agents = list(parse_environment(self.filename)[1].keys())
        
        self.timestep = None
        self.miscoordinations = None

    def reset(self, seed=None, options=None):
        self.agents = copy(self.possible_agents)
        self.timestep = 0
        self.miscoordinations = 0
        self.gridworld, self.robot_pos, self.robot_goals = parse_environment(self.filename)
        
        observations = { a: self.robot_pos[a][0] + len(self.gridworld) * self.robot_pos[a][1] for a in self.agents } 
        
        # Get dummy infos. Necessary for proper parallel_to_aec conversion
        
        infos = {a: {} for a in self.agents}
        
        return observations, infos

    def step(self, actions, coordination):
        next_pos = []
        agent_penalty = dict()
        for agent in self.agents:
            agent_penalty[agent] = False
            agent_action = actions[agent]
            if np.random.uniform() > 0.2:
                current_pos = self.robot_pos[agent]
                if agent_action == "N":
                    self.robot_pos[agent] = current_pos[0], current_pos[1] - 1
                if agent_action == "S":
                    self.robot_pos[agent] = current_pos[0], current_pos[1] + 1
                if agent_action == "W":
                    self.robot_pos[agent] = current_pos[0] - 1, current_pos[1]
                if agent_action == "E":
                    self.robot_pos[agent] = current_pos[0] + 1, current_pos[1]

            x, y = self.robot_pos[agent]
            in_doorway = True if self.gridworld[y][x] == "D" else False

            if self.robot_pos[agent] in next_pos and in_doorway:
                for a in self.agents:
                    if self.robot_pos[a] == self.robot_pos[agent]:
                        agent_penalty[a] = True

                next_pos.append(self.robot_pos[agent])

        terminations = {a: False for a in self.agents}
        rewards = {a: -0.5 for a in self.agents}
        
        for a in self.agents:
            if self.robot_pos[a] == self.robot_goals[a]:
                rewards[a] += 10
                terminations[a] = True
            if agent_penalty[a]:
                rewards[a] -= 20
            if coordination[a]:
                rewards[a] -= 1
           
        self.timestep += 1      
        truncations = {a: False for a in self.agents}
        if self.timestep > 99:
            rewards = {a: -0.5 for a in self.agents}
            truncations = {a: True for a in self.agents}
        


        observations = { a: self.robot_pos[a][0] + len(self.gridworld) * self.robot_pos[a][1] for a in self.agents } 
        
        # Get dummy infos. Necessary for proper parallel_to_aec conversion
        
        infos = {a: {} for a in self.agents}      
        
        if any(terminations.values()) or all(truncations.values()):
            self.agents = []
            
        return observations, rewards, terminations, truncations, infos
        

    def render(self):
        copy_environment = deepcopy(self.gridworld)
        for robot in self.agents:
            x, y = self.robot_pos[robot]
            copy_environment[y][x] = "*"
            print(f"\n{robot}: ({x}, {y})")
            x, y = self.robot_goals[robot]
            copy_environment[y][x] = "*"
            print(f"goal{robot[-1:]}: ({x}, {y})")
        print("\n")
        for j in copy_environment:
            line = ""
            for i in j:
                line += i + " "
            print(line +"\n")

            
    def get_agents(self):
        return self.agents

    # Observation space should be defined here.
    # lru_cache allows observation and action spaces to be memoized, reducing clock cycles required to get each agent's space.
    # If your spaces change over time, remove this line (disable caching).
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        # gymnasium spaces are defined and documented here: https://gymnasium.farama.org/api/spaces/
        states = self.get_num_states()
        return MultiDiscrete([states])

    def get_num_states(self):
        states = 0
        for j in self.gridworld:
            for i in j:
                if i in ["_", "D"]:
                    states += 1
        return states
    
    def get_grid(self):
        return self.gridworld


    # Action space should be defined here.
    # If your spaces change over time, remove this line (disable caching).
    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return Discrete(4)