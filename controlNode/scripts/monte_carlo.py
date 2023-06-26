import random
import time

def monte_carlo_pi(num_samples):
    count = 0
    for i in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / num_samples

if __name__ == '__main__':
    # Number of samples
    num_samples = 100000000

    # Start time
    start_time = time.time()

    # Compute pi
    pi = monte_carlo_pi(num_samples)

    # End time
    end_time = time.time()

    # Print result
    print(f"Pi: {pi}")
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")

