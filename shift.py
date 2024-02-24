def shift(nums):
    """
    This function takes a list of numbers as input and shifts all elements one position to the left, 
    deleting the last element, and returns the first element of the original list. If the input list 
    is empty, the function returns None.

    Args:
        nums (list): The list of numbers to be shifted.

    Returns:
        The first element of the original list or None if the list is empty.
    """
    if not nums:
        return None

    first = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    del nums[-1]
    return first


result = shift([1, 2, 3, 4, 5])
print(result)  # Output: 1

result = shift([])
print(result)  # Output: None

