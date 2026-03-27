import random
from fitness import fitness


POP_SIZE = 10
DIM = 4
MAX_ITER = 20


def random_solution():
    return [random.randint(10, 60) for _ in range(DIM)]


def optimize():

    population = [random_solution() for _ in range(POP_SIZE)]

    best = population[0]
    best_score = fitness(best)
    history = []
    for it in range(MAX_ITER):

        for i in range(POP_SIZE):
            score = fitness(population[i])

            if score < best_score:
                best_score = score
                best = population[i]

        history.append(best_score)

        # move grasshoppers (simple version)
        for i in range(POP_SIZE):

            for d in range(DIM):

                population[i][d] += random.randint(-5, 5)

                if population[i][d] < 5:
                    population[i][d] = 5

                if population[i][d] > 60:
                    population[i][d] = 60

        print("Iter", it, "Best =", best_score)

    return best, best_score, history