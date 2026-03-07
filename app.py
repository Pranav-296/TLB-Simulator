import streamlit as st

from src.simulator import run_simulation
from src.address_generator import generate_sequential, generate_random, generate_locality


st.title("TLB Simulator Web Interface")

pattern = st.selectbox(
    "Access Pattern",
    ["sequential", "random", "locality"]
)

n = st.slider("Number of Memory Accesses", 5, 100, 20)

tlb_size = st.slider("TLB Size", 2, 16, 4)

page_size = st.slider("Page Size", 2, 16, 4)

policy = st.selectbox(
    "Replacement Policy",
    ["FIFO", "LRU"]
)

if st.button("Run Simulation"):

    if pattern == "sequential":
        addresses = generate_sequential(n)

    elif pattern == "random":
        addresses = generate_random(n, 50)

    else:
        addresses = generate_locality(n)

    hits, misses = run_simulation(
        addresses,
        tlb_size,
        policy,
        page_size,
        experiment_mode=True
    )

    total = hits + misses

    hit_ratio = hits / total
    miss_rate = misses / total

    st.subheader("Results")

    st.write("Total Accesses:", total)
    st.write("TLB Hits:", hits)
    st.write("TLB Misses:", misses)
    st.write("Hit Ratio:", round(hit_ratio,3))
    st.write("Miss Rate:", round(miss_rate,3))
