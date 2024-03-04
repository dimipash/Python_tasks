def remove_duplicates(numbers):
    """
    This function removes duplicate elements from a list of numbers. The function first sorts the list, 
    then iterates over the sorted list and appends each number to the result list only if it's not equal 
    to the previous number.

    Parameters:
    numbers (list): The list of numbers from which to remove duplicates.

    Returns:
    list: The list of numbers with duplicates removed.
    """
    numbers.sort()
    result = []
    previous = None

    for num in numbers:
        if num != previous:
            result.append(num)
            previous = num

    return result


def compare(list1, list2):
    """
    This function compares two lists of numbers for equality after removing duplicates from each list.

    Parameters:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.

    Returns:
    bool: True if the lists are equal after removing duplicates, False otherwise.
    """
    list1 = remove_duplicates(list1)
    list2 = remove_duplicates(list2)

    return list1 == list2

print(compare([1, 2, 3, 3, 4], [1, 2, 2, 3]))  # Output: False
