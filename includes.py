def includes(arr, search_element, from_index=0):
    """
    This function takes a list, a search element, and an optional from_index as input. 
    It returns True if the search element is found in the list starting from the from_index, 
    and False otherwise.

    Args:
        arr (list): The list in which to search for the element.
        search_element: The element to search for in the list.
        from_index (int, optional): The index from which to start the search. Default is 0.

    Returns:
        bool: True if the search element is found in the list, False otherwise.
    """
    return search_element in arr[from_index:]


result = includes([1, 2, 3, 0, 12], 3)
print(result)  # Output: True

result = includes([1, 2, 3, 0, 12], 1)
print(result)  # Output: True

result = includes([1, 2, 3, 0, 12], 4)
print(result)  # Output: False

