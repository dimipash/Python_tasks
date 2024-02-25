def subarray(arr, start, end=None):
    """
    This function returns a subarray of a given array starting from a specified index to an end index.
    If the end index is not provided, it returns the subarray from the start index to the end of the array.

    Parameters:
    arr (list): The array to get the subarray from.
    start (int): The start index of the subarray.
    end (int, optional): The end index of the subarray. 
                         If not provided, the subarray goes to the end of the array.

    Returns:
    list: The subarray from the start index to the end index.
    """
   
    end = len(arr) if end is None else end

    return arr[start:end]

arr = [1, 2, 3, 3, 3]
print(subarray(arr, 2))  # Output: [3, 3, 3]

arr = [1, 2, 3, 4, 3]
print(subarray(arr, 2, 4))  # Output: [3, 4]

