def find_two_numbers_with_product(nums, target):
    """Find two numbers in the given list that multiply to the target value."""
    seen = {}

    for i, num in enumerate(nums):
        if target == 0:
            if nums.count(0) >= 2:
                return [i for i, n in enumerate(nums) if n == 0][:2]
            return None

        if num != 0 and target % num == 0:
            complement = target // num
            if complement in seen:
                return [seen[complement], i]

        seen[num] = i

    return None


print(find_two_numbers_with_product([2, 3, 5, 10], 15))
print(find_two_numbers_with_product([1, 5, 7], 35))
print(find_two_numbers_with_product([6, 8, 4, 2], 12))
