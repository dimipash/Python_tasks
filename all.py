def new_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print(new_all([True, 1, 'a']))  # True
print(new_all([True, 0, 'a']))  # False
