from environment import Environment
from independant_learners import independant_learning
from joint_action_learner import joint_action_learner
from plot import plot_graph

EPISODES = 10000
DECAY = 9/10
MINIMUM_EPSILON = 0.1
RUNS = 7


FILENAMES = ["grid1.txt", "grid2.txt", "grid3.txt"]
ALGORITHMS = [independant_learning]

def experiment():

    for filename in FILENAMES:
        avg_time = [[0 for i in range(EPISODES)] for i in range(len(ALGORITHMS))]
        avg_rewards = [[0 for i in range(EPISODES)] for i in range(len(ALGORITHMS))]
        avg_miscoordinations = [[0 for i in range(EPISODES)] for i in range(len(ALGORITHMS))]
        
        for run in range(RUNS):
            for alg in range(len(ALGORITHMS)):
                time, rewards, miscoordinations = independant_learning(filename, EPISODES, DECAY, MINIMUM_EPSILON)
                for episode in range(EPISODES):
                    avg_time[alg][episode] += time[episode] / RUNS
                    avg_rewards[alg][episode] += rewards[episode] / RUNS
                    avg_miscoordinations[alg][episode] += miscoordinations[episode] / RUNS
            
        plot_graph(filename, "Timstep graph", "Timestep", avg_time)
        plot_graph(filename, "Rewards graph", "Average rewards", avg_rewards)
        plot_graph(filename, "Miscoordinations graph", "Miscoordinations", avg_miscoordinations)
    
experiment()