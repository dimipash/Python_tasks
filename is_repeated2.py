def sub_compare(s, p1, p2, len):
    """
        This function compares two substrings of equal length from the same string.

        Args:
            s (str): The string from which substrings are to be compared.
            p1 (int): The starting index of the first substring.
            p2 (int): The starting index of the second substring.
            len (int): The length of the substrings to be compared.

        Returns:
            bool: Returns True if the substrings are identical, False otherwise.
        """
    for p in range(0, len):
        if s[p1 + p] != s[p2 + p]:
            return False
    return True


def is_repeated(st):
    """
        This function checks if a string consists of one or more repetitions of a substring.

        Args:
            st (str): The string to be checked for repetitions.

        Returns:
            bool: Returns True if the string consists of one or more repetitions of a substring, False otherwise.
        """
    for s_len in range(1, len(st) // 2 + 1):
        if len(st) % s_len != 0:
            continue

        for j in range(s_len, len(st), s_len):
            if not sub_compare(st, 0, j, s_len):
                break
        else:
            return True

    return False


print(is_repeated("abc"))  # False
print(is_repeated("1212"))  # True
print(is_repeated("alaala"))  # True
print(is_repeated("alaal"))  # False
print(is_repeated("zzzzz"))  # True
print(is_repeated("acacac"))  # True
print(is_repeated("acaca"))  # False
