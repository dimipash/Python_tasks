def decimal_to_hex(num):
    """
    This function takes a decimal number as input and returns its hexadecimal 
    representation as a string. The function uses a while loop to repeatedly 
    divide the number by 16 and prepend the remainder to the result string.

    Args:
        num (int): The decimal number to be converted into hexadecimal.

    Returns:
        str: The hexadecimal representation of the input number.
    """
    if num == 0:
        return "0"

    hex_chars = "0123456789abcdef"
    result = ""

    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num //= 16

    return result


print(decimal_to_hex(5))  # Output: '5'
print(decimal_to_hex(10))  # Output: 'a'
print(decimal_to_hex(16))  # Output: '10'
print(decimal_to_hex(255))  # Output: 'ff'


