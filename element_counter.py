"""
This class implements a counter to efficiently count the occurrences of elements within an iterable object.

Attributes:
    counts (dict): A dictionary storing element counts as key-value pairs.

Raises:
    ValueError: If the input to the constructor is not an iterable object.
"""


class Counter:
    def __init__(self, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("Input must be an iterable")
        self.counts = {}
        for item in iterable:
            self.counts[item] = self.counts.get(item, 0) + 1

    def __getitem__(self, item):
        return self.counts.get(item, 0)

    def __repr__(self):
        sorted_counts = sorted(self.counts.items(), key=lambda x: -x[1])
        return f"Counter({sorted_counts})"


list = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
c = Counter(list)
print(c)  # Counter({'x': 4, 'y': 2, 'z': 2})
print(c['x'])  # 4


