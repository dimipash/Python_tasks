"""
Demonstrates the use of the 'all()' function in Python.

Shows examples of 'all()' with:
1. Checking if all numbers in a list are positive.
2. Verifying if all strings in a list have length greater than 3.
3. Checking if all files in a list of file paths exist.
"""

numbers = [1, 2, 3, 4]
print(all(num > 0 for num in numbers))  # True

strings = ["apple", "banana", "cherry"]
print(all(len(s) > 3 for s in strings))  # True

import os

file_paths = ["file1.txt", "file2.txt", "file3.txt"]
print(all(os.path.exists(path) for path in file_paths))
