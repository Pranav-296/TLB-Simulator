def hit_ratio(hits, total):
    if total == 0:
        return 0
    return hits / total


def miss_rate(misses, total):
    if total == 0:
        return 0
    return misses / total


def calculate_amat(hit_time, miss_rate, miss_penalty):
    return hit_time + (miss_rate * miss_penalty)
