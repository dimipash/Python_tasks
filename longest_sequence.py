def find_longest_consecutive_sequence(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Input must be a list')
    for element in input_list:
        if not isinstance(element, int):
            raise ValueError('All elements in the list must be integers')

    max_seq = seq = []

    for number in input_list:
        if seq and number == seq[-1] + 1:
            seq.append(number)
        else:
            seq = [number]
        if len(seq) > len(max_seq):
            max_seq = seq

    return max_seq


print(find_longest_consecutive_sequence([0, 5, 1, 2, 3, 4, 5, 2, 8, 9, 10]))  # Output: [1, 2, 3, 4, 5]
