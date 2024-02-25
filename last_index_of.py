def last_index_of(arr, value, from_index=None):
    """
    This function returns the last index of a given value in an array. 
    If the value is not found, it returns -1.

    Parameters:
    arr (list): The array to search.
    value (any): The value to find.
    from_index (int, optional): The index to start the search from. 
                                If not provided, the search starts from the end of the array.

    Returns:
    int: The last index of the value in the array, or -1 if the value is not found.
    """
   
    from_index = from_index if from_index else len(arr) - 1

    for i in range(from_index, -1, -1):
        if arr[i] == value:
            return i
    return -1

arr = [1, 0, 3, 0, 12]
print(last_index_of(arr, 0))  # Output: 3

arr = [1, 0, 3, 0, 12]
print(last_index_of(arr, 0, 2))  # Output: 1

arr = [1, 2, 3, 0, 12]
print(last_index_of(arr, 4))  # Output: -1

