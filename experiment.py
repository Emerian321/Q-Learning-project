from environment import Environment
from independant_learners import independant_learning

EPISODES = 10000
DECAY = 9/10
MINIMUM_EPSILON = 0.1
RUNS = 7


FILENAMES = ["grid1.txt", "grid2.txt", "grid3.txt"]

def experiment():
    res = []
    for filename in FILENAMES:
        for run in range(RUNS):
            independant_learning(filename, EPISODES, DECAY, MINIMUM_EPSILON)
        

experiment()