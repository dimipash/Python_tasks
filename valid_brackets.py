pairs = {')': '(', '}': '{', ']': '['}
opening = set(pairs.values())


def valid_brackets(string):
    """
    This function checks if a string has valid bracket pairs.

    Args:
        string (str): The string to check.

    Returns:
        bool: Returns True if the string has valid bracket pairs, False otherwise.
    """
    stack = []
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in pairs.keys():
            if not stack or pairs[char] != stack.pop():
                return False
    return not stack


print(valid_brackets("()"))  # True
print(valid_brackets("()[]{}"))  # True
print(valid_brackets("(]"))  # False
print(valid_brackets("([)]"))  # False
print(valid_brackets("{[]}"))  # True
print(valid_brackets("Hello (world)!"))  # True
print(valid_brackets("aa {aa} [aa]!"))  # True
print(valid_brackets("bb)!"))  # False
