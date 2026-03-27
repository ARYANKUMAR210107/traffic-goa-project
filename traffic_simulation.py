import numpy as np

np.random.seed(42)

def generate_traffic_data(condition="medium"):
    ranges = {
        "low":    (5,  10),
        "medium": (10, 20),
        "high":   (20, 30),
    }
    low, high = ranges.get(condition, ranges["medium"])
    return np.random.randint(low, high + 1, size=4)

def traffic_simulation(green_times, condition="medium"):

    arrival_rate = generate_traffic_data(condition)

    total_delay = 0
    queue_length = 0

    for i in range(4):

        cars = arrival_rate[i]
        green = green_times[i]

        if cars > green:
            delay = (cars - green) * 2
        else:
            delay = cars / green

        total_delay += delay
        queue_length += max(0, cars - green)

    return total_delay + queue_length