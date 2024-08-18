"""
Demonstrates the use of the 'any()' function in Python.

Illustrates 'any()' with:
1. Checking if any number in a list is truthy.
2. Verifying if any number in a list is positive.
3. Checking if any string in a list is empty.
4. Determining if any file in a list of file paths exists.
"""

numbers = [0, 1, 2, 3, 4]
print(any(numbers))  # True

numbers2 = [-1, -2, 0, -4]
print(any(num > 0 for num in numbers2))  # False

strings = ["apple", "", "banana"]
print(any(s == "" for s in strings))  # True

import os

file_paths = ["file1.txt", "file2.txt", "file3.txt"]
print(any(os.path.exists(path) for path in file_paths))
