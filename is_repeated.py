def is_repeated(s):
    """
    This function checks if a string is composed of repeated substrings.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is composed of repeated substrings, False otherwise.
    """
   
    for i in range(1, len(s)):
        if s == s[:i] * (len(s) // i):
            return True
    return False



print(is_repeated("abc"))  # False
print(is_repeated("1212"))  # True
print(is_repeated("alaala"))  # True
print(is_repeated("alaal"))  # False
print(is_repeated("zzzzz"))  # True
print(is_repeated("acacac"))  # True
print(is_repeated("acaca"))  # False
