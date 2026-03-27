import matplotlib.pyplot as plt


def plot_graph(values):

    plt.figure()
    plt.plot(values)
    plt.xlabel("Iteration")
    plt.ylabel("Best Delay")
    plt.title("GOA Convergence Graph")


def plot_comparison(normal, goa, ga):

    methods = ["Normal", "GOA", "GA"]
    values = [normal, goa, ga]

    plt.figure()
    plt.bar(methods, values)
    plt.xlabel("Method")
    plt.ylabel("Delay")
    plt.title("Algorithm Comparison")