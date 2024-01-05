import matplotlib.pyplot as plt

def plot_graph(filename, graph_title, ylabel, dataset):

    plt.scatter(range(1, len(dataset[0])+1), dataset[0], label='Independant Learners', alpha=0.1)
    plt.scatter(range(1, len(dataset[1])+1), dataset[1], label='Joint-Action Learner', alpha=0.1)
    plt.scatter(range(1, len(dataset[2])+1), dataset[2], label='Sparse Cooperative algorithm', alpha=0.1)
    
    plt.xlabel('Episodes')
    plt.ylabel(ylabel)
    plt.title(graph_title + "in environment" + filename)
    plt.legend()
    plt.show()