def most_common_letters(text, n):
    """
    This function finds the n most common letters in a given text. The function is case-insensitive and 
    only considers alphabetic characters. If multiple letters have the same frequency, the function 
    chooses the lexicographically largest one.

    Parameters:
    text (str): The text in which to find the most common letters.
    n (int): The number of most common letters to find.

    Returns:
    list: A list of the n most common letters in the text, in order of decreasing frequency.
    """
   
    text = text.lower()
    counter = {}

    for letter in text:
        if 'a' <= letter <= 'z':
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

    most_common = []
    for _ in range(n):
        max_count = max(counter.values())
        max_letters = []
        for letter, count in counter.items():
            if count == max_count:
                max_letters.append(letter)
        most_common.append(max(max_letters))
        for letter in max_letters:
            del counter[letter]

    return most_common


print(most_common_letters("Hello World", 3))  # ['l', 'o', 'w']


