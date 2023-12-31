import random 



class MDPAgent():

    def __init__(self, env, epsilon, gamma, alpha, numTraining, episode):

        self.environment = env
        self.epsilon = epsilon
        self.gamma = gamma
        self.alpha = alpha
        self.numTraining = numTraining
        self.episode = episode
        self.Qvalues = {}

    def getQvalue(self, state, action):
        return self.Qvalues.setdefault(state, {action:0 for action in self.getLegalActions(state)})[action]

    """
    Returns max_action of all Q(state,action) of every legal actions, or 0 if none exist.
    """
    def computeValueFromQvalue(self, state):

        return max([self.getQValue(state, action) for action  in self.getLegalActions(state)], default=0)

    """
    Compute the best action to take in a state.  Note that if there
    are no legal actions, which is the case at the terminal state,
    you should return None.
    """
    def computeActionFromQValues(self, state):

        return max([(self.getQValue(state, action), action) for action  in self.getLegalActions(state)], default=(0, None))[1]


    """
    Compute the action to take in the current state.  With
    probability self.epsilon, we should take a random action and
    take the best policy action otherwise.  Note that if there are
    no legal actions, which is the case at the terminal state, you
    should choose None as the action.
    """
    def getAction(self, state):

        if random.random()>self.epsilon:
          return random.choice([action for action in self.getLegalActions(state)])
        else:
          return self.computeActionFromQValues(state)



    def getLegalActions(self, state):
        actions = self.environment.getLegalActions(state)
        return actions
    

    """    
    update the qV of one state action with the knowledge of the reward
    """
    def update(self, state, action, nextState, reward):

      self.Qvalues[state][action] = self.getQValue(state, action) + \
      self.alpha * (reward + self.discount * self.computeValueFromQValues(nextState) -  self.getQValue(state, action))

