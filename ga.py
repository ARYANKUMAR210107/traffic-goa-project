import numpy as np
from fitness import fitness

POP_SIZE   = 10
ITERATIONS = 50
N_SIGNALS  = 4
LOW, HIGH  = 5, 60
MUTATION_RATE = 0.2


def _init_population():
    return np.random.randint(LOW, HIGH + 1, size=(POP_SIZE, N_SIGNALS))


def _select(population, scores):
    i, j = np.random.choice(POP_SIZE, 2, replace=False)
    return population[i] if scores[i] < scores[j] else population[j]


def _crossover(parent1, parent2):
    point = np.random.randint(1, N_SIGNALS)
    return np.concatenate([parent1[:point], parent2[point:]])


def _mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        idx = np.random.randint(N_SIGNALS)
        individual[idx] = np.random.randint(LOW, HIGH + 1)
    return individual


def ga_optimize():
    population = _init_population()

    best_solution = None
    best_score = float("inf")

    for _ in range(ITERATIONS):
        scores = np.array([fitness(ind) for ind in population])

        # Track best
        min_idx = np.argmin(scores)
        if scores[min_idx] < best_score:
            best_score = scores[min_idx]
            best_solution = population[min_idx].copy()

        # Build next generation
        next_population = []
        for _ in range(POP_SIZE):
            parent1 = _select(population, scores)
            parent2 = _select(population, scores)
            child   = _crossover(parent1, parent2)
            child   = _mutate(child)
            next_population.append(child)

        population = np.array(next_population)

    return best_solution, best_score
