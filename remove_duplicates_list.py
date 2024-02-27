def remove_duplicates(numbers):
    """
    This function removes all duplicate elements from a list, preserving the original order of elements.

    Parameters:
    numbers (list): The list of numbers from which to remove duplicates.

    Returns:
    list: A list with all duplicates removed.
    """
    seen = set()
    result = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result

nums = [1, 3, 8, 1, 16, 3, 4]
print(remove_duplicates(nums))  # Output: [1, 3, 8, 16, 4]
