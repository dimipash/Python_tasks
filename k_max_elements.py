def k_max_elements(nums, k):
    """
    This function finds the k maximum unique elements in a list. 
    If k is greater than or equal to the length of the list, it returns all unique elements in the list.

    Parameters:
    nums (list): The list of numbers.
    k (int): The number of maximum unique elements to find.

    Returns:
    list: A list of the k maximum unique elements.
    """
    result = []
    seen = set()

    if k >= len(nums):
        result = list(set(nums))

    else:
        nums_copy = nums.copy()
        while len(result) < k:
            max_num = max(nums_copy)
            if max_num not in seen:
                seen.add(max_num)
                result.append(max_num)
            nums_copy.remove(max_num)

    return result

print(k_max_elements([1, 8, 8, 0, 6, 3, 6, 6], 9)) 
