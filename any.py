def new_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(new_any([True, 1, 'a']))  # True
print(new_any([False, 0, None]))  # False
