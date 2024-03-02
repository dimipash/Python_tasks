def close_values(nums1, nums2):
    """
    This function checks if every number in the longer list (nums2 if not equal length) is either equal to, 
    one less than, or one more than a number in the shorter list (nums1 if not equal length).

    Parameters:
    nums1 (list): The first list of numbers.
    nums2 (list): The second list of numbers.

    Returns:
    bool: True if every number in the longer list is either equal to, one less than, or one more than a number in the shorter list. False otherwise.
    """
   
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    s1 = set(nums1)
    for n2 in nums2:
        if n2 - 1 in s1 or n2 in s1 or n2 + 1 in s1:
            continue
        else:
            return False
    return True

print(close_values([1, 3, 5], [2, 4, 6]))  # Output: True
print(close_values([1, 3, 5], [2, 4]))  # Output: True
print(close_values([1, 3, 5], [2]))  # Output: False
print(close_values([1, 3, 5], [2, 4, 7]))  # Output: False
