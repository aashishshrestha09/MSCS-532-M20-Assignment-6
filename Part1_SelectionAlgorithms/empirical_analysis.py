import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Callable
import random

from deterministic_selection import deterministic_select
from randomized_selection import randomized_select
from utils.dataset_utils import generate_test_data
from utils import file_utils


def time_algorithm(
    algorithm: Callable[[list[int], int], int],
    arr: list[int],
    k: int,
    repeats: int = 7,
    rand_gen: random.Random = None,
) -> float:
    """
    Measures the average execution time (in milliseconds) of the given selection algorithm
    over multiple runs to provide a stable timing measurement.

    Args:
        algorithm (Callable): The selection function to test.
        arr (list[int]): The input list to select from.
        k (int): The k-th order statistic to find (0-based index).
        repeats (int): Number of times to repeat timing for averaging.
        rand_gen (random.Random, optional): Random generator instance for deterministic randomness.

    Returns:
        float: Average execution time in milliseconds over all repeats.
    """
    times = []
    for _ in range(repeats):
        arr_copy = arr.copy()  # Prevent in-place modification affecting later runs
        start_time = time.perf_counter()

        # Use fixed random generator if provided for randomized_select to ensure reproducibility
        if rand_gen and algorithm == randomized_select:
            algorithm(arr_copy, k, rand_gen)
        else:
            algorithm(arr_copy, k)

        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    return sum(times) / len(times)  # Return average time


def run_benchmarks(
    input_sizes: list[int] = [1000, 2000, 4000, 8000, 16000, 32000],
    data_types: list[str] = ["random", "sorted", "reversed"],
):
    """
    Runs performance benchmarks on both randomized and deterministic selection algorithms
    across different input sizes and data distributions.

    Args:
        input_sizes (list[int]): List of input sizes to test.
        data_types (list[str]): List of data distributions to test.

    Returns:
        pd.DataFrame: DataFrame containing benchmark results.
    """
    results = []

    # Use a fixed-seed random generator for consistent randomized algorithm behavior
    rand_gen = random.Random(42)

    for data_type in data_types:
        for size in input_sizes:
            data = generate_test_data(size, data_type)
            k = size // 2  # Median index

            # Time randomized algorithm with fixed randomness
            randomized_time = time_algorithm(
                randomized_select, data, k, rand_gen=rand_gen
            )

            # Time deterministic algorithm (no randomness)
            deterministic_time = time_algorithm(deterministic_select, data, k)

            results.append(
                {
                    "Size": size,
                    "Distribution": data_type,
                    "Randomized (ms)": randomized_time,
                    "Deterministic (ms)": deterministic_time,
                }
            )

    # Convert results to DataFrame for analysis and visualization
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False))

    # Save results to CSV for record keeping
    file_utils.save_dataframe_to_csv(df, "selection_benchmark_results.csv")

    # Plot and save performance graph for randomized select
    sns.lineplot(data=df, x="Size", y="Randomized (ms)", hue="Distribution", marker="o")
    plt.title("Randomized Select Performance")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    file_utils.save_plot_to_file("randomized_select_performance.png")
    plt.clf()

    # Plot and save performance graph for deterministic select
    sns.lineplot(
        data=df, x="Size", y="Deterministic (ms)", hue="Distribution", marker="o"
    )
    plt.title("Deterministic Select Performance")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    file_utils.save_plot_to_file("deterministic_select_performance.png")
    plt.clf()

    return df


if __name__ == "__main__":
    run_benchmarks()
