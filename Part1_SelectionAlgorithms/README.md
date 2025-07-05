# Part 1: Medians and Order Statistics Selection Algorithms

## Overview

This project implements and benchmarks selection algorithms for finding the k-th smallest element in a list:

- **Randomized Quickselect** (Expected O(n))
- **Deterministic Median of Medians** (Worst-case O(n))

It also explores implementations of fundamental data structures including Arrays, Stacks, Queues, and Singly Linked Lists.  
Tools for generating test data, benchmarking performance, saving results, and plotting graphs are included.  
Unit tests are provided using Python’s built-in `unittest` framework to verify correctness.

## 📦 Project Structure

```bash
.
├── __init__.py
├── deterministic_selection.py      # Deterministic Median of Medians algorithm
├── empirical_analysis.py           # Benchmark runner + result graphing and saving
├── outputs                         # Auto-generated CSV and PNG files
│   ├── deterministic_select_performance_<timestamp>.png
│   ├── randomized_select_performance_<timestamp>.png
│   └── selection_benchmark_results_<timestamp>.csv
├── randomized_selection.py         # Randomized Quickselect algorithm
├── README.md
├── tests                           # Unit tests for both selection algorithms
│   ├── __init__.py
│   └── test_selection_algorithms.py
└── utils
    ├── __init__.py
    ├── dataset_utils.py            # Test dataset generation utilities
    └── file_utils.py               # CSV and plot saving utilities
```

## Setup

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

### Clone the repository

If you haven't cloned the repository yet, run:

```bash
git clone https://github.com/aashishshrestha09/MSCS-532-M20-Assignment-6.git
cd MSCS-532-M20-Assignment-6
```

> [!TIP]
> If you already have the repository cloned, navigate to its root directory before proceeding.

### Create and Activate a Virtual Environment:

If you don't already have an active virtual environment, create and activate one with:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### Install as editable with "dev" packages

```bash
pip install --editable ".[dev]"
```

## Usage

### 📈 Run Benchmarks

```bash
python Part1_SelectionAlgorithms/empirical_analysis.py
```

- Benchmark results printed in the terminal as a markdown table.
- CSV files and performance plots saved automatically in `Part1_SelectionAlgorithms/outputs/`.

### Run Unit Tests

Run all unit tests to validate correctness:

```bash
python -m unittest discover Part1_SelectionAlgorithms/tests
```

## Benchmark Features

- Test dataset sizes: 1000, 2000, 4000, 8000, 16000, 32000
- Data distributions: Random, Sorted, Reverse-sorted
- Measures average runtime (ms) for each selection algorithm
- CSV + performance plots automatically saved to outputs/ directory with timestamps

## Algorithms Implemented

- Randomized Quickselect: Expected O(n)
- Deterministic Median of Medians: Worst-case O(n)

## Summary of Findings

- Randomized Quickselect is consistently faster in practice due to its lower overhead and expected linear time, though it has a rare worst-case of O(n²).
- Deterministic Median of Medians guarantees linear time in the worst case by carefully choosing pivots but has higher constant overhead, making it slower in average-case scenarios.
- Benchmark results across varying data sizes and distributions confirm theoretical expectations.
- For practical purposes, Randomized Quickselect is preferred unless worst-case guarantees are required.

## Data Structures

Implemented:

- Arrays
- Stacks (using arrays)
- Queues (using arrays)
- Singly Linked Lists

Observations:

- Arrays provide constant-time access but require shifting elements on insertion/deletion.
- Stacks and Queues were efficiently implemented using arrays.
- Singly Linked Lists offer constant-time insertion/deletion at the head but require traversal for other operations.
