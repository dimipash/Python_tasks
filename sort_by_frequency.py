def sort_by_frequency(arr):
    """
        This function sorts the elements in an array based on their frequency in descending order.
        If two elements have the same frequency, the one which appears first in the array will come first.

        Args:
            arr (list): The list of integers to be sorted.

        Returns:
            list: Returns a list of integers sorted by frequency.
    """
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    sorted_arr = []
    max_count = max(counts.values())
    for i in range(max_count, 0, -1):
        for num in counts:
            if counts[num] == i:
                sorted_arr.extend([num] * i)

    return sorted_arr


print(sort_by_frequency([2, 3, 5, 3, 7, 9, 5, 3, 7]))
print(sort_by_frequency([2, 1, 2]))
print(sort_by_frequency([2, 1, 2, 1]))
