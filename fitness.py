from traffic_simulation import traffic_simulation

def fitness(solution):

    # solution = [g1, g2, g3, g4]

    delay = traffic_simulation(solution)

    return delay