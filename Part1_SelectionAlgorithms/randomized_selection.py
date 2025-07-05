import random


def partition(arr: list[int], low: int, high: int, pivot_index: int) -> int:
    """
    Partitions the array around the pivot element chosen at pivot_index.
    Elements less than pivot are moved before it; elements greater after it.

    Args:
        arr (list[int]): The list to partition.
        low (int): Starting index of the partition segment.
        high (int): Ending index of the partition segment.
        pivot_index (int): Index of the pivot element.

    Returns:
        int: The final index of the pivot after partitioning.
    """
    pivot_value = arr[pivot_index]
    # Move pivot to end temporarily
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    store_index = low  # Pointer for final pivot placement

    for i in range(low, high):
        if arr[i] < pivot_value:
            # Swap element smaller than pivot to the front partition
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Move pivot to its final sorted position
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index


def randomized_select(arr: list[int], k: int, rand_gen: random.Random = None) -> int:
    """
    Selects the k-th smallest element in arr using the randomized Quickselect algorithm.
    Expected time complexity: O(n).

    Args:
        arr (list[int]): List of integers from which to select.
        k (int): Zero-based index (0 <= k < len(arr)) of the order statistic to find.
        rand_gen (random.Random, optional): Random generator instance for deterministic randomness.
                                            If None, default random is used.

    Returns:
        int: The k-th smallest element in the list.
    """
    # Base case: only one element left
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot index using provided random generator or default
    if rand_gen:
        pivot_index = rand_gen.randint(0, len(arr) - 1)
    else:
        pivot_index = random.randint(0, len(arr) - 1)

    # Partition array around pivot and get its final index
    new_pivot_index = partition(arr, 0, len(arr) - 1, pivot_index)

    # Recursively select from correct partition based on k
    if k == new_pivot_index:
        return arr[new_pivot_index]
    elif k < new_pivot_index:
        return randomized_select(arr[:new_pivot_index], k, rand_gen)
    else:
        return randomized_select(
            arr[new_pivot_index + 1 :], k - new_pivot_index - 1, rand_gen
        )
