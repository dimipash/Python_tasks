def union(set1, set2):
    """
    This function returns the union of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The union of set1 and set2.
    """
    result = set()
    for item in set1:
        result.add(item)
    for item in set2:
        result.add(item)
    return result


def intersect(set1, set2):
    """
    This function returns the intersection of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The intersection of set1 and set2.
    """
    result = set()
    for item in set1:
        if item in set2:
            result.add(item)
    return result


def diff(set1, set2):
    """
    This function returns the difference of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The difference of set1 and set2.
    """
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result


def symmetrical_diff(set1, set2):
    """
    This function returns the symmetrical difference of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The symmetrical difference of set1 and set2.
    """
    return union(diff(set1, set2), diff(set2, set1))
