from src.simulator import run_simulation
from src.address_generator import generate_locality


def run_experiment():

    accesses = generate_locality(50)

    tlb_sizes = [2, 4, 8]
    policies = ["FIFO", "LRU"]

    print("\nTLB Experiment Results")
    print("------------------------------")
    print("TLB Size | Policy | Hit Ratio")
    print("------------------------------")

    for size in tlb_sizes:
        for policy in policies:

            hits, misses = run_simulation(accesses, size, policy, experiment_mode=True)

            total = hits + misses
            ratio = hits / total

            print(size, "     |", policy, "  |", round(ratio,3))


if __name__ == "__main__":
    run_experiment()
