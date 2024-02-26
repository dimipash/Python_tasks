def common_chars(s1, s2):
    """
    This function finds the common characters between two strings in the order they appear in the first string. 
    If a character appears more than once in both strings, it appears in the result as many times as it appears in both strings.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    str: A string of common characters between s1 and s2.
    """
    result = []
    s2_chars = list(s2)

    for char in s1:
        if char in s2_chars:
            result.append(char)
            s2_chars.remove(char)

    return ''.join(result)

print(common_chars("abc", "def"))  # Output: ""
print(common_chars("abc", "cde"))  # Output: "c"
print(common_chars("abc", "dafc"))  # Output: "ac"
print(common_chars("abca", "deaf"))  # Output: "a"



