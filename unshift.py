def unshift(arr, element):
    """
    This function takes a list and an element as input. It inserts the element at the beginning 
    of the list and shifts all other elements to the right. If the list is empty, the function 
    simply appends the element to the list. The function modifies the input list in-place and 
    does not return anything.

    Args:
        arr (list): The list in which to insert the element.
        element: The element to be inserted at the beginning of the list.
    """
    if len(arr) == 0:
        arr.append(element)
        return
    last_el = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = element
    arr.append(last_el)


arr = [1, 2, 3, 0, 12]
unshift(arr, 8)
print(arr)  # Output: [8, 1, 2, 3, 0, 12]

