def index_of(text, word, from_index=0):
    """
    This function returns the first index of a given word in a text starting from a specified index. 
    If the word is not found, it returns -1.

    Parameters:
    text (str): The text to search.
    word (str): The word to find.
    from_index (int, optional): The index to start the search from. 
                                If not provided, the search starts from the beginning of the text.

    Returns:
    int: The first index of the word in the text starting from the specified index, or -1 if the word is not found.
    """
   
    if from_index > len(text) or from_index < 0:
        return -1

    length_word = len(word)

    for i in range(from_index, len(text)):
        if text[i:i + length_word] == word:
            return i

    return -1

print(index_of("ala bala", "la"))  # Output: 1

print(index_of("github", "hub"))  # Output: 3

print(index_of("microsoft", "google"))  # Output: -1

