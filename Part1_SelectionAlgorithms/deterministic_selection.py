def partition(arr: list[int], low: int, high: int, pivot_index: int) -> int:
    """
    Partitions the array around the pivot element.
    """
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low

    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index


def median_of_medians(arr: list[int], low: int, high: int) -> int:
    """
    Selects a good pivot using the Median of Medians strategy.
    """
    n = high - low + 1
    if n < 5:
        return sorted(arr[low : high + 1])[n // 2]

    medians = []
    i = low
    while i <= high:
        group = arr[i : min(i + 5, high + 1)]
        medians.append(sorted(group)[len(group) // 2])
        i += 5

    return deterministic_select(medians, len(medians) // 2)


def deterministic_select(arr: list[int], k: int) -> int:
    """
    Returns the k-th smallest element in arr using the deterministic
    Median of Medians algorithm in worst-case linear time.
    """
    if len(arr) == 1:
        return arr[0]

    pivot_value = median_of_medians(arr, 0, len(arr) - 1)
    pivot_index = partition(arr, 0, len(arr) - 1, arr.index(pivot_value))

    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return deterministic_select(arr[:pivot_index], k)
    else:
        return deterministic_select(arr[pivot_index + 1 :], k - pivot_index - 1)
