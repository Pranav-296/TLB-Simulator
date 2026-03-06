# TLB-Simulator
# TLB Simulator

A Python-based Translation Lookaside Buffer (TLB) simulator that demonstrates
virtual-to-physical address translation and evaluates TLB performance under
different memory access patterns and replacement policies.

## Features
- FIFO and LRU replacement policies
- Sequential, random, and locality access patterns
- TLB hit/miss analysis
- Average Memory Access Time (AMAT)
- Experiment mode for policy comparison

## Run Simulator
python3 -m src.simulator

## Run Experiments
python3 -m src.experiment
