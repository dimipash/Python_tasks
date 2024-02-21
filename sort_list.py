def sort_list(numbers):
    """
    This function sorts a list of integers in ascending order using counting sort. 
    It assumes that the input list contains only integers from 0 to 5 (inclusive). 
    The function modifies the input list in-place and does not return anything.

    Args:
        numbers (list): The list of integers to be sorted.
    """
    numbers_count = [0, 0, 0, 0, 0, 0]

    for num in numbers:
        numbers_count[num] += 1

    numbers.clear()
    for num, count in enumerate(numbers_count):
        for _ in range(count):
            numbers.append(num)


numbers = [1, 3, 1, 2, 5, 2, 1, 3]
sort_list(numbers)
print(numbers)  # Output: [1, 1, 1, 2, 2, 3, 3, 5]

numbers = [1, 3, 3, 2, 5, 1, 1, 4]
sort_list(numbers)
print(numbers)  # Output: [1, 1, 1, 2, 3, 3, 4, 5]

