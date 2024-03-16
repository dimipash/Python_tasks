def first_unique_letter(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


print(first_unique_letter("alabala"))  # 3
print(first_unique_letter("github"))  # 0
print(first_unique_letter("alabalab"))  # 1


