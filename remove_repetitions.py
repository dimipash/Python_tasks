def remove_repetitions(nums):
    """
        This function removes the repeated elements from a list, preserving the original order of appearance.

        Args:
            nums (list): The list of integers from which repetitions are to be removed.

        Returns:
            list: Returns a list of integers with repetitions removed.
    """
    seen = set()
    index = 0

    for n in nums:
        if n in seen:
            break
        index += 1
        seen.add(n)

    for i in range(index, len(nums)):
        n = nums[i]
        if n in seen:
            continue
        nums[index] = n
        index += 1
        seen.add(n)

    for _ in range(len(nums) - index):
        nums.pop()

    return nums


print(remove_repetitions([3, 12, 5, 12, 8, 5]))  # Output: [3, 12, 5, 8]
print(remove_repetitions([1, 2, 3, 2, 1]))  # Output: [1, 2, 3]
