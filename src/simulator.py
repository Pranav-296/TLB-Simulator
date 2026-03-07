from address_generator import generate_sequential, generate_random, generate_locality
from metrics import hit_ratio, miss_rate, calculate_amat


class TLB:

    def __init__(self, size, policy="FIFO"):
        self.size = size
        self.entries = []
        self.policy = policy

    def lookup(self, page):

        if page in self.entries:

            # LRU update: move page to most recent
            if self.policy == "LRU":
                self.entries.remove(page)
                self.entries.append(page)

            return True

        return False


    def insert(self, page):

        if len(self.entries) >= self.size:

            # FIFO replacement
            if self.policy == "FIFO":
                self.entries.pop(0)

            # LRU replacement
            elif self.policy == "LRU":
                self.entries.pop(0)

        self.entries.append(page)


class PageTable:

    def lookup(self, page):
        return page


def run_simulation(addresses, tlb_size, policy):

    tlb = TLB(tlb_size, policy)
    page_table = PageTable()

    hits = 0
    misses = 0

    for address in addresses:

        page = address

        if tlb.lookup(page):
            hits += 1

        else:
            misses += 1
            frame = page_table.lookup(page)
            tlb.insert(frame)

    total = hits + misses

    hr = hit_ratio(hits, total)
    mr = miss_rate(misses, total)

    amat = calculate_amat(
        hit_time=1,
        miss_rate=mr,
        miss_penalty=100
    )

    print("\nTLB Simulation Results")
    print("----------------------")
    print("Replacement Policy:", policy)
    print("Total Accesses:", total)
    print("TLB Hits:", hits)
    print("TLB Misses:", misses)
    print("Hit Ratio:", round(hr, 3))
    print("Miss Rate:", round(mr, 3))
    print("Average Memory Access Time:", amat)


def main():

    print("\nTLB Simulator")

    pattern = input("Access pattern (sequential/random/locality): ")

    n = int(input("Number of memory accesses: "))
    tlb_size = int(input("TLB size: "))
    policy = input("Replacement policy (FIFO/LRU): ").upper()

    if pattern == "sequential":
        addresses = generate_sequential(n)

    elif pattern == "random":
        addresses = generate_random(n, 10)

    else:
        addresses = generate_locality(n)

    print("\nAddress Stream:", addresses)

    run_simulation(addresses, tlb_size, policy)


if __name__ == "__main__":
    main()
