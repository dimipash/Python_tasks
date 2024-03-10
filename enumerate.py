def new_enumerate(iterable, start=0):
    n = start
    result = []
    for element in iterable:
        result.append((n, element))
        n += 1
    return result


print(new_enumerate([1, 2, 3]))  # [(0, 1), (1, 2), (2, 3)]
