def ip_to_int(ip_addr):
    """
    This function takes an IPv4 address as a string and returns an integer that represents 
    the IP address. Each part of the IP address is shifted and combined to form the integer.

    Args:
        ip_addr (str): The IPv4 address as a string.

    Returns:
        int: The integer representation of the IPv4 address.
    """
    ip_parts = ip_addr.split('.')
    a, b, c, d = [int(part) for part in ip_parts]

    result = (a << 24) | (b << 16) | (c << 8) | d

    return result


print(ip_to_int('255.255.255.255'))  # Output: 4294967295
print(ip_to_int('0.0.0.1'))  # Output: 1
print(ip_to_int('0.0.1.0'))  # Output: 256




