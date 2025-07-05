#!/usr/bin/env python3
"""
run_all.py

Root-level script to run benchmarks and unit tests for both parts
of Assignment 6: Medians and Order Statistics & Elementary Data Structures.

This script automates:
- Part 1: Running empirical benchmarks and unit tests.
- Part 2: Running unit tests.

Usage:
    python run_all.py

Exit Codes:
    0 - All tasks completed successfully
    1 - One or more tasks failed
"""

import subprocess
import sys


def run_command(command: str, description: str) -> None:
    """
    Run a shell command and handle errors gracefully.

    Args:
        command (str): The shell command to run.
        description (str): Description of the task being executed.

    Raises:
        SystemExit: Exits with status 1 if the command fails.
    """
    print(f"\n>>> Starting: {description}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f">>> Completed: {description}\n")
    except subprocess.CalledProcessError:
        print(f">>> ERROR: {description} failed")
        sys.exit(1)


def main() -> None:
    """
    Main function to run all benchmarks and tests in sequence.
    """
    # Run Part 1: Selection Algorithms Benchmarks
    run_command(
        "python Part1_SelectionAlgorithms/empirical_analysis.py",
        "Part 1: Selection Algorithms Benchmarks",
    )

    # Run Part 1: Unit Tests
    run_command(
        "python -m unittest discover Part1_SelectionAlgorithms/tests",
        "Part 1: Unit Tests",
    )

    # Run Part 2: Data Structures Unit Tests
    run_command(
        "python -m unittest discover Part2_DataStructures/tests",
        "Part 2: Data Structures Unit Tests",
    )

    print(">>> All tasks completed successfully!")


if __name__ == "__main__":
    main()
