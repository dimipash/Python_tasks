"""
Demonstrates the use of enumerate() function in Python.

Iterates over a list of names, creating numbered output.
Uses enumerate() to generate both index and value in the loop.
The 'start' parameter is set to 1 for one-based indexing.
"""

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
