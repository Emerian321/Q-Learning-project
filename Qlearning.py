import numpy as np

ACTIONS = ["N", "S", "W", "E"]

class Qlearner:
    def __init__(self, name, env, learning_rate=0.7, discount_factor=0.99, exploration_rate=1):

        self.name = name
        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        gridsize = len(env.get_grid())
        self.q_table = dict()
        for y in range(gridsize):
            for x in range(gridsize):
                if self.env.get_grid()[y][x] in ["_", "D"]:
                    self.q_table[x + gridsize * y] = self.compute_legal_actions(x, y, gridsize)
                     
                
    def compute_legal_actions(self, x, y, size):
        res = []
        # North
        if y - 1 in range(size):
            if self.env.get_grid()[y - 1][x] in ["_", "D"]:
                res.append(0)
            else:
                res.append(-float("inf")) 
        else:
            res.append(-float("inf")) 
        
        # South  
        if y + 1 in range(size):
            if self.env.get_grid()[y + 1][x] in ["_", "D"]:
                res.append(0)
            else:
                res.append(-float("inf")) 
        else:
            res.append(-float("inf")) 
        
        # West   
        if x - 1 in range(size):
            if self.env.get_grid()[y][x - 1] in ["_", "D"]:
                res.append(0)
            else:
                res.append(-float("inf")) 
        else:
            res.append(-float("inf")) 
        
        # East    
        if x + 1 in range(size):
            if self.env.get_grid()[y][x + 1] in ["_", "D"]:
                res.append(0)
            else:
                res.append(-float("inf")) 
        else:
            res.append(-float("inf")) 
        
        return res
    
    def get_next_action(self, state):
        #if a randomly chosen value between 0 and 1 is less than epsilon, 
        #then choose the most promising value from the Q-table for this state.
        if np.random.random() > self.exploration_rate:
            return ACTIONS[np.argmax(self.q_table[state])]
        else: #choose a random action
            action = float("-inf")
            while action == float("-inf"):
                action = np.random.choice(self.q_table[state])
            return ACTIONS[self.q_table[state].index(action)]
        
    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        current_q_value = self.q_table[state][ACTIONS.index(action)]

        # Q-learning update rule

        new_q_value = current_q_value + self.learning_rate * (reward + self.discount_factor * self.q_table[next_state][best_next_action] - current_q_value)

        # Update Q-value in the Q-table
        self.q_table[state][ACTIONS.index(action)] = new_q_value
        
    def refresh_epsilon(self, decay_rate, minimum):
        self.exploration_rate = max(self.exploration_rate * decay_rate, minimum)
    
    
    def get_name(self):
        return self.name
        