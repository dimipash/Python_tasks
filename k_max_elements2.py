def k_max_elements(numbers, k):
    if k > len(numbers):
        raise ValueError("k must be less than the length of nums")

    set_numbers = set(numbers[:k + 1])
    for idx in range(k, len(numbers)):
        set_min = min(set_numbers)
        if numbers[idx] > set_min and numbers[idx] not in set_numbers:
            set_numbers.remove(set_min)
            set_numbers.add(numbers[idx])
    return list(set_numbers)


print(k_max_elements([1, 8, 8, 0, 6, 3, 6, 6], 3))