def remove_char(text, position):
    """
    This function removes a character from a given position in a string.

    Parameters:
    text (str): The string from which to remove the character.
    position (int): The position of the character to remove.

    Returns:
    str: The string with the character removed.

    Raises:
    IndexError: If the position is greater than the length of the string.
    """
   
    if position > len(text):
        raise IndexError("Position out of range.")
    return text[:position] + text[position + 1:]

print(remove_char("albala", 2))  # Output: "alala"

