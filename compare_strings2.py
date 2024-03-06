def compare_strings(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    length = len(s1)
    index = 0

    for i in range(length):
        if s1[i] == ' ':
            continue
        if s1[i].lower() not in s2.lower():
            return False
        if s1[i].lower() == s2[index].lower():
            index += 1

    return True


print(compare_strings("  abc  ", "abc"))
print(compare_strings("ABC", "abc"))
print(compare_strings(" ala   bala", "ala bala"))
print(compare_strings(" ала bala  ", "alabala"))
