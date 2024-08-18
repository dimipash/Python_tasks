"""
Demonstrates the use of Counter from the collections module.

Creates a Counter object to count occurrences of words in a list.
Prints the resulting frequency distribution of words.
"""

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)
print(count)
