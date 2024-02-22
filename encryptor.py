def encryptor(word, n):
    """
    This function takes a string and a number as input and returns a new string 
    where each character in the input string is shifted 'n' places to the right in the alphabet. 
    This is a simple implementation of the Caesar cipher encryption technique.

    Args:
        word (str): The string to be encrypted.
        n (int): The number of places to shift each character in the string.

    Returns:
        str: The encrypted string.
    """
    encrypted = ""
    for char in word:
        new_ord = ord(char) + n
        if new_ord > 122:
            new_ord -= 26
        encrypted += chr(new_ord)
    return encrypted


print(encryptor('abc', 3))  # Output: 'def'
print(encryptor('zab', 2))  # Output: 'bcd'




