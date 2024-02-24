def index_of(arr, element, from_index=0):
    """
    This function takes a list, an element, and an optional from_index as input. 
    It returns the index of the first occurrence of the element in the list starting 
    from the from_index. If the element is not found in the list, it returns -1.

    Args:
        arr (list): The list in which to search for the element.
        element: The element to search for in the list.
        from_index (int, optional): The index from which to start the search. Default is 0.

    Returns:
        int: The index of the first occurrence of the element in the list starting from the from_index, 
             or -1 if the element is not found.
    """
    if element in arr:
        return arr.index(element, from_index)
    else:
        return -1


result = index_of([1, 2, 3, 0, 3, 12], 3, 3)
print(result)  # Output: 4

result = index_of([1, 2, 3, 0, 12], 1)
print(result)  # Output: 0

result = index_of([1, 2, 3, 0, 12], 4)
print(result)  # Output: -1

