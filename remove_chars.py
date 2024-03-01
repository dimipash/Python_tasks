def remove_chars(text, *chars_to_remove):
    """
    This function removes specified characters from a string.

    Parameters:
    text (str): The string from which to remove characters.
    chars_to_remove (str): The characters to remove from the string.

    Returns:
    str: The string with the specified characters removed.
    """
   
    chars_set = set(chars_to_remove)
    new_text = []
    for char in text:
        if char not in chars_set:
            new_text.append(char)
    return "".join(new_text)

print(remove_chars("alabala", 'a', 'b'))  # Output: "ll"

