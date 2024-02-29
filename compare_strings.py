def compare_strings(s1, s2):
    """
    This function compares two strings for equality, ignoring case and whitespace.

    Parameters:
    s1 (str): The first string to compare.
    s2 (str): The second string to compare.

    Returns:
    bool: True if the strings are equal (ignoring case and whitespace), False otherwise.
    """

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return s1 == s2


print(compare_strings("  abc  ", "abc"))  # Output: True
print(compare_strings("ABC", "abc"))  # Output: True
print(compare_strings(" ala   bala", "ala bala"))  # Output: True
print(compare_strings(" ала bala  ", "alabala"))  # Output: False

