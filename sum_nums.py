def sum_nums(arr):
    """
    This function takes a list of numbers as input and returns a new list 
    where each element is the cumulative sum of the elements in the input list up to that point.

    Args:
        arr (list): The list of numbers to be summed.

    Returns:
        list: A list containing the cumulative sums of the elements of the input list.
    """
    totals = []
    total = 0
    for num in arr:
        total += num
        totals.append(total)
    return totals


result = sum_nums([1, 3])
print(*result, sep=', ')  # Output: 1, 4

result = sum_nums([1, 2, 3])
print(*result, sep=', ')  # Output: 1, 3, 6

result = sum_nums([2, -1, 8])
print(*result, sep=', ')  # Output: 2, 1, 9


