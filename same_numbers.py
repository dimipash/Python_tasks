def same_numbers(arr1, arr2):
    """
    This function checks if two arrays have the same numbers, regardless of their count or order.

    Parameters:
    arr1 (list): The first array to compare.
    arr2 (list): The second array to compare.

    Returns:
    bool: True if both arrays have the same numbers, False otherwise.
    """
   
    return set(arr1) == set(arr2)

result = same_numbers([1, 1, 2, 3], [1, 2, 2, 2, 3])
print(result)  # Output: True

result = same_numbers([1, 2, 3, 3, 3], [2, 2, 2, 4])
print(result)  # Output: False

