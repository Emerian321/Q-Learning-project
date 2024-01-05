def joint_action_learner(filename, num_episodes, decay_rate, min_epsilon):
    
    times = [0 for i in range(num_episodes)]
    avg_rewards = [0 for i in range(num_episodes)]
    miscoordinations = [0 for i in range(num_episodes)]
    
    return times, avg_rewards, miscoordinations