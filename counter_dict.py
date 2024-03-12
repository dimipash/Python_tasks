from functools import reduce


def counter_dict(res, val):
    """
        This function counts the frequency of each character in a string.

        Args:
            res (dict): The dictionary to store the count of each character.
            val (str): The character to count.

        Returns:
            dict: The updated dictionary with the count of the character.
    """
    res[val] = res.get(val, 0) + 1
    return res


s = "hello world"
c = reduce(counter_dict, s, {})
print(c)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
