class Counter:
    """
    This class represents a collection of items with their counts.

    The class can be initialized with an iterable or a dictionary of items and their counts.
    It provides methods to update the counts, access the count of an item, and get a string representation of the collection.

    Attributes:
        counts (dict): A dictionary mapping items to their counts.
    """
    def __init__(self, iterable=None, **kwargs):
        self.counts = {}

        if iterable is not None:
            if isinstance(iterable, dict):
                self.counts.update(iterable)
            else:
                self.update(iterable)

        self.counts.update(kwargs)

    def update(self, iterable):
        for item in iterable:
            if item in self.counts:
                self.counts[item] += 1
            else:
                self.counts[item] = 1

    def __getitem__(self, item):
        return self.counts.get(item, 0)

    def __repr__(self):
        sorted_counts = sorted(self.counts.items(), key=lambda x: -x[1])
        return f"Counter({sorted_counts})"


c = Counter()
print(c)

c = Counter('gallahad')
print(c)

c = Counter({'red': 4, 'blue': 2})
print(c)

c = Counter(cats=4, dogs=8)
print(c)
