def set_bit(num, index):
    return num | (1 << index)


def clear_bit(num, index):
    return num & ~(1 << index)


def toggle_bit(num, index):
    return num ^ (1 << index)


def get_bit(num, index):
    return (num & (1 << index)) != 0


print(set_bit(1, 1))  # 3
print(set_bit(0, 2))  # 4

print(clear_bit(3, 0))  # 2
print(clear_bit(7, 1))  # 5

print(toggle_bit(0, 1))  # 2
print(toggle_bit(5, 0))  # 4

print(get_bit(5, 0))  # True
print(get_bit(4, 0))  # False
