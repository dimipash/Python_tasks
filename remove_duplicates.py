def remove_duplicates(numbers):
    """
    This function removes consecutive duplicate numbers from a list.

    Parameters:
    numbers (list): The list of numbers from which to remove duplicates.

    Returns:
    list: A list with consecutive duplicates removed.
    """
    result = []
    previous = None

    for num in numbers:
        if num != previous:
            result.append(num)
            previous = num

    return result

output = remove_duplicates([1, 2, 3, 3, 4, 4, 5])
print(output)  # Output: [1, 2, 3, 4, 5]
