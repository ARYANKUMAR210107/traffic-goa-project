from goa import optimize
from ga import ga_optimize
from plot import plot_graph, plot_comparison
from flowchart import draw_flowchart
from traffic_simulation import traffic_simulation
import matplotlib.pyplot as plt


normal = [30, 30, 30, 30]

normal_delay = traffic_simulation(normal, "medium")

print("Normal delay:", normal_delay)


# GOA
best_goa, score_goa, history = optimize()

print("\nGOA RESULT")
print("Best timing =", best_goa)
print("Best delay =", score_goa)


# GA
best_ga, score_ga = ga_optimize()

print("\nGA RESULT")
print("Best timing =", best_ga)
print("Best delay =", score_ga)


draw_flowchart()
plt.show()

plot_graph(history)
plt.show()

plot_comparison(normal_delay, score_goa, score_ga)
plt.show()