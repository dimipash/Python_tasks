def common_chars(str1, str2):
    """
    This function takes two strings as input and returns a string that contains all the characters 
    that appear in both strings, in the order they appear in the second string. Each character in 
    the output string appears only once, even if it appears multiple times in the input strings.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: A string containing the common characters between str1 and str2.
    """
    output = ''
    memo = set(str1)
    for char in str2:
        if char in memo:
            output += char
            memo.remove(char)
    return output

result = common_chars("abc", "def")
print(result)  # Output: ''

result = common_chars("abc", "cde")
print(result)  # Output: 'c'

result = common_chars("abc", "dafc")
print(result)  # Output: 'ac'

result = common_chars("abca", "deaf")
print(result)  # Output: 'a'

