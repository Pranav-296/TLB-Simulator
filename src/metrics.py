# Calculate TLB hit ratio
def hit_ratio(hits, total):
    if total == 0:
        return 0
    return hits / total


# Calculate miss rate
def miss_rate(misses, total):
    if total == 0:
        return 0
    return misses / total


# Calculate Average Memory Access Time
def calculate_amat(hit_time, miss_rate, miss_penalty):
    return hit_time + (miss_rate * miss_penalty)
