# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Overview

This repository contains implementations and analyses for **Assignment 6** of the MSCS-532-M20 course.

It includes:

- **Part 1:** Algorithms for medians and order statistics, featuring randomized and deterministic selection algorithms with empirical benchmarking.
- **Part 2:** Elementary data structures implemented from scratch, including arrays, stacks, queues, singly linked lists, and rooted trees, with accompanying unit tests.

For detailed setup instructions, execution steps, findings, graphs, and outputs, refer to the README file in each part’s directory:

- [Part1_SelectionAlgorithms/README.md](Part1_SelectionAlgorithms/README.md)
- [Part2_DataStructures/README.md](Part2_DataStructures/README.md)

## Project Structure

```bash
.
├── Part1_SelectionAlgorithms
│   ├── __init__.py
│   ├── deterministic_selection.py
│   ├── empirical_analysis.py
│   ├── outputs
│   │   ├── deterministic_select_performance.png_20250705_103819.png
│   │   ├── randomized_select_performance.png_20250705_103819.png
│   │   └── selection_benchmark_results.csv_20250705_103818.csv
│   ├── randomized_selection.py
│   ├── README.md
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_selection_algorithms.py
│   └── utils
│       ├── __init__.py
│       ├── dataset_utils.py
│       └── file_utils.py
├── Part2_DataStructures
│   ├── __init__.py
│   ├── array_and_matrix.py
│   ├── README.md
│   ├── rooted_tree.py
│   ├── singly_linked_list.py
│   ├── stack_and_queue.py
│   └── tests
│       ├── __init__.py
│       └── test_data_structures.py
├── pyproject.toml
├── README.md
└── run_all.py
```

## Getting Started

## Prerequisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

### Setup

1. Clone the repository:

```bash
git clone https://github.com/aashishshrestha09/MSCS-532-M20-Assignment-6.git
cd MSCS-532-M20-Assignment-6
```

2. Create and activate a virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
```

3. Install project dependencies

```bash
pip install --editable ".[dev]"
```

## Usage Overview

To run all benchmarks and unit tests for both parts of this assignment with a single command, use the provided root script:

```bash
python run_all.py
```

This script will:

- Execute empirical benchmarks and unit tests for Part 1: Selection Algorithms.
- Execute unit tests for Part 2: Elementary Data Structures.

For detailed usage instructions for each part, please refer to their respective README files:

- [Part1_SelectionAlgorithms/README.md](./Part1_SelectionAlgorithms/README.md)
- [Part2_DataStructures/README.md](./Part2_DataStructures/README.md)
