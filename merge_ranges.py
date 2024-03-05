def merge_ranges(ranges):
    """
    This function takes a list of ranges and merges any overlapping ranges.

    Args:
        ranges (list of lists): Each inner list contains two integers representing the start and end of a range.

    Returns:
        list of lists: Returns a new list of ranges where overlapping ranges have been merged.
    """
    result = []

    curr_start = ranges[0][0]
    curr_end = ranges[0][1]

    for start, end in ranges[1:]:
        if start > curr_end:
            result.append([curr_start, curr_end])
            curr_start = start
            curr_end = end
        else:
            curr_end = max(curr_end, end)

    result.append([curr_start, curr_end])
    return result



print(merge_ranges([[1, 5], [2, 4]]))  # [[1, 5]]
print(merge_ranges([[1, 5], [6, 8]]))  # [[1, 5], [6, 8]]
print(merge_ranges([[1, 5], [5, 6]]))  # [[1, 6]]
print(merge_ranges([[1, 5], [4, 7], [6, 8]]))  # [[1, 8]]
