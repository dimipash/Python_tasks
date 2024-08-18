"""
Demonstrates two methods of combining lists in Python:
1. Using the '+' operator for list addition.
2. Using itertools.chain() for lazy and memory-efficient combination.

Compares the output and characteristics of both methods.
"""

from itertools import chain

# List addition
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combine_add = list1 + list2  # Immediate and memory-intensive

# itertools.chain
combined_chain = chain(list1, list2)  # Lazy and efficient

print(combine_add)
print(combined_chain)
