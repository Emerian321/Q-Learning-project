from Qlearning import Qlearner
from environment import Environment
import numpy as np



def independant_learning(filename, num_episodes, decay_rate, min_epsilon):
    env = Environment(filename)
    state, _ = env.reset()
    agents = [Qlearner(a, env) for a in env.get_agents()]
    coordination = {a: False for a in env.get_agents()}
    times = []
    
    for episode in range(num_episodes):
        state, _ = env.reset()
        done = False
        timestep = 0
        actions = dict()
        terminated = {a: False for a in env.get_agents()}
        
        while not done:
            for agent in agents:
                name = agent.get_name()
                if not terminated[name]:
                    actions[name] = agent.get_next_action(state[name])
            next_state, rewards, terminations, truncation, _ = env.step(actions, coordination)
            
            for agent in agents:
                name = agent.get_name()
                if not terminated[name]:
                    agent.update(state[name], actions[name], rewards[name], next_state[name])
                if terminations[name]:
                    terminated[name] = True
                
            done = any(terminations.values()) or all(truncation.values())
            state = next_state

        times.append(env.timestep)

        for agent in agents:
            agent.refresh_epsilon(decay_rate, min_epsilon)

    return times



    