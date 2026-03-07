import random

# Sequential access pattern
def generate_sequential(n):
    return list(range(n))


# Random access pattern
def generate_random(n, max_page):
    return [random.randint(0, max_page) for _ in range(n)]


# Locality-based pattern
def generate_locality(n):
    base_pattern = [1, 2, 3, 1, 2, 3, 4]
    result = []

    while len(result) < n:
        result.extend(base_pattern)

    return result[:n]
