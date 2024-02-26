def delete_chars(text):
    """
    This function processes a string and removes the character before the '#' symbol. 
    If the '#' symbol is at the beginning of the string or if there are multiple '#' symbols in a row, 
    it simply removes the '#' symbol.

    Parameters:
    text (str): The string to process.

    Returns:
    str: The processed string with the characters before '#' symbols removed.
    """
    result = []

    for char in text:
        if char == "#":
            if result:
                result.pop()
            continue
        result.append(char)
    return "".join(result)

print(delete_chars("abc#"))  # Output: "ab"
print(delete_chars("a#bc"))  # Output: "bc"
print(delete_chars("abc##"))  # Output: "a"
print(delete_chars("a##bc"))  # Output: "bc"
