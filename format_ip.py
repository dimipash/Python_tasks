def format_ip(last_4_bytes):
    """
    This function takes an integer as input and returns a string that represents 
    an IPv4 address. The integer is split into four bytes, and each byte represents 
    one part of the IPv4 address.

    Args:
        last_4_bytes (int): The integer to be converted into an IPv4 address.

    Returns:
        str: The IPv4 address as a string.
    """
    ip4 = last_4_bytes & 0xff
    ip3 = (last_4_bytes >> 8) & 0xff
    ip2 = (last_4_bytes >> 16) & 0xff
    ip1 = (last_4_bytes >> 24) & 0xff

    return f'{ip1}.{ip2}.{ip3}.{ip4}'


print(format_ip(1))  # Output: '0.0.0.1'
print(format_ip(256))  # Output: '0.0.1.0'
print(format_ip(65535))  # Output: '0.0.255.255'


