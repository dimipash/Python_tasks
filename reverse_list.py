def sort_list(arr):
    """
    This function takes a list of elements as input and returns a new list 
    that contains all the elements of the input list in reverse order.

    Args:
        arr (list): The list of elements to be reversed.

    Returns:
        list: A list containing the elements of the input list in reverse order.
    """
    reversed_list = []

    for i in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list


result = sort_list([1, 2, 3, 4])
print(*result, sep=' ')

