from src.address_generator import generate_sequential, generate_random, generate_locality
from src.metrics import hit_ratio, miss_rate, calculate_amat


class TLB:

    def __init__(self, size, policy="FIFO"):
        self.size = size
        self.entries = []
        self.policy = policy

    def lookup(self, page):

        if page in self.entries:

            # update order for LRU
            if self.policy == "LRU":
                self.entries.remove(page)
                self.entries.append(page)

            return True

        return False


    def insert(self, page):

        if len(self.entries) >= self.size:
            self.entries.pop(0)

        self.entries.append(page)



class PageTable:

    def lookup(self, page):
        return page   # simple page → frame mapping



def run_simulation(addresses, tlb_size, policy, page_size, experiment_mode=False):

    tlb = TLB(tlb_size, policy)
    page_table = PageTable()

    hits = 0
    misses = 0

    if not experiment_mode:
        print("\nAccess | Address | Page | Offset | Result | TLB State")
        print("-------------------------------------------------------")

    for i, address in enumerate(addresses):

        page = address // page_size
        offset = address % page_size

        if tlb.lookup(page):

            hits += 1
            result = "HIT"

        else:

            misses += 1
            frame = page_table.lookup(page)
            tlb.insert(frame)
            result = "MISS"

        if not experiment_mode:
            print(f"{i+1:5} | {address:7} | {page:4} | {offset:6} | {result:5} | {tlb.entries}")


    total = hits + misses

    hr = hit_ratio(hits, total)
    mr = miss_rate(misses, total)

    amat = calculate_amat(
        hit_time=1,
        miss_rate=mr,
        miss_penalty=100
    )

    if experiment_mode:
        return hits, misses


    print("\nTLB Simulation Results")
    print("----------------------")
    print("Replacement Policy:", policy)
    print("Total Accesses:", total)
    print("TLB Hits:", hits)
    print("TLB Misses:", misses)
    print("Hit Ratio:", round(hr,3))
    print("Miss Rate:", round(mr,3))
    print("Average Memory Access Time:", amat)

    return hits, misses



def main():

    print("\nTLB Simulator")

    pattern = input("Access pattern (sequential/random/locality): ")

    n = int(input("Number of memory accesses: "))
    tlb_size = int(input("TLB size: "))
    page_size = int(input("Page size: "))
    policy = input("Replacement policy (FIFO/LRU): ").upper()


    if pattern == "sequential":
        addresses = generate_sequential(n)

    elif pattern == "random":
        addresses = generate_random(n, 50)

    else:
        addresses = generate_locality(n)


    run_simulation(addresses, tlb_size, policy, page_size)


if __name__ == "__main__":
    main()
