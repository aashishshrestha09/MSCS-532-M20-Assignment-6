# Part 2: Elementary Data Structures

## Overview

This module implements fundamental data structures from scratch in Python:

- **Arrays**
- **Stacks** (implemented using arrays)
- **Queues** (implemented using arrays)
- **Singly Linked Lists**
- **Rooted Trees** (optional implementation using linked nodes)

Each data structure supports standard operations such as insertion, deletion, access, and traversal. Comprehensive unit tests validate correctness and ensure reliability.

## Project Structure

```bash
.
├── __init__.py
├── array_and_matrix.py
├── README.md
├── rooted_tree.py
├── singly_linked_list.py
├── stack_and_queue.py
└── tests
    ├── __init__.py
    └── test_data_structures.py
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

### Run Unit Tests

To run unit tests for all data structures:

```bash
python -m unittest discover Part2_DataStructures/tests
```

## Performance Analysis

- Arrays: Provide O(1) access time, but insertion and deletion may require shifting elements (O(n) time).
- Stacks & Queues: Efficiently implemented using arrays with O(1) average time for push/pop or enqueue/dequeue operations
- Singly Linked Lists: Allow O(1) insertion and deletion at the head, but traversal and searching are O(n).
- Rooted Trees: Represent hierarchical relationships; traversal complexity depends on tree size and structure.

## Practical Applications

- Arrays are ideal for indexed access where fixed-size collections are handled.
- Stacks are commonly used for function call management, undo mechanisms, and expression evaluation.
- Queues enable task scheduling, buffering, and breadth-first search implementations.
- Singly Linked Lists are useful when dynamic memory allocation is needed with frequent insertions and deletions, especially at the list head.
- Rooted Trees are used to represent hierarchical data such as file systems, organizational charts, and XML/HTML DOM structures.

## Summary

This module offers foundational data structure implementations designed to help understand their inner workings, performance characteristics, and practical use cases. The included unit tests facilitate robust validation and easy extension.
