"""
Demonstrates the use of defaultdict from the collections module.

Uses defaultdict to count occurrences of words in a list.
Initializes counts to 0 and increments them for each word.
Prints the resulting word frequency dictionary.
"""

from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
words_count = defaultdict(int)

for word in words:
    words_count[word] += 1

print(dict(words_count))
