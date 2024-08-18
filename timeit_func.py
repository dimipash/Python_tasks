"""
Compares performance of list comprehension vs. map() for doubling list elements.

Uses timeit to measure execution time of both methods over 100,000 iterations.
"""

import timeit

# Implementation 1: List Comprehension
code1 = """
a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a]
"""


# Implementation 2: Map function
def code2():
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x: x * 2, a))


time1 = timeit.timeit(code1, number=100000)  # by default runs 1M times
time2 = timeit.timeit(code2, number=100000)

print(f"List comprehension time: {time1}")
print(f"Map function time: {time2}")
