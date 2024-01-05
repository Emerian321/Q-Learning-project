from environment import Environment
from Qlearning import Qlearner

def sparse_interaction_algorithm(filename, num_episodes, decay_rate, min_epsilon):
    env = Environment(filename)
    state, _ = env.reset()
    agents = [Qlearner(a, env) for a in env.get_agents()]
    coordination = {a: False for a in env.get_agents()}
    times = []
    avg_rewards = []
    miscoordinations = []
    
    for episode in range(num_episodes):
        state, _ = env.reset()
        actions = dict()
        done = False
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
                    actions[name] = None
                
            done = all(terminated.values()) or all(truncation.values())
            state = next_state

        times.append(env.timestep)
        avg_rewards.append(calculate_rewards(agents))
        miscoordinations.append(env.miscoordinations)

        for agent in agents:
            agent.refresh_epsilon(decay_rate, min_epsilon)
    return times, avg_rewards, miscoordinations


def calculate_rewards(agents):
    res = 0
    for agent in agents:
        for rewards in agent.q_table.values():
            for reward in rewards:
                if reward != float("-inf"):
                    res += reward / len(agents)
    return res