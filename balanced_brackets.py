"""
This function determines if a string contains valid balanced parentheses.

Args:
    s (str): The input string containing brackets.

Returns:
    bool: True if the brackets are balanced, False otherwise.

Raises:
    ValueError: If the input is not a string.
"""


def valid_brackets(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[stack.pop()] != char:
            return False
    return not stack


print(valid_brackets("()"))  # True
print(valid_brackets("()[]{}"))  # True
print(valid_brackets("(]"))  # False
print(valid_brackets("([)]"))  # False
print(valid_brackets("{[]}"))  # True
