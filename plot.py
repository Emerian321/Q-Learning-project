import matplotlib.pyplot as plt
import numpy as np


def plot_graph(filename, graph_title, ylabel, dataset):
    x = np.linspace(1, len(dataset[0])+1, len(dataset[0]))
    y = dataset[0]
    # fit a linear curve and estimate its y-values and their error.
    a, b = np.polyfit(x, y, deg=1)
    y_est = a * x + b
    y_err = x.std() * np.sqrt(1/len(x) +
                            (x - x.mean())**2 / np.sum((x - x.mean())**2))

    fig, ax = plt.subplots()
    ax.plot(x, y_est, '-')
    ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
    ax.plot(x, y, 'o', color='tab:brown')

    
    plt.xlabel('Episodes')
    plt.ylabel(ylabel)
    plt.title(graph_title + " in environment " + filename)
    plt.legend()
    plt.show()

