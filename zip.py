def new_zip(*iterables):
    min_length = min(len(iterable) for iterable in iterables)
    zipped = []

    for i in range(min_length):
        zipped_tuple = []
        for iterable in iterables:
            zipped_tuple.append(iterable[i])
        zipped.append(tuple(zipped_tuple))

    return zipped


print(new_zip([1, 2], [3, 4], [5, 6]))  # [(1, 3, 5), (2, 4, 6)]
