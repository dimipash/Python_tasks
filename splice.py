def splice(arr, start, count=None, *insert_items):
    if count is None:
        count = len(arr) - start

    for i in range(count):
        if start < len(arr) - i:
            item_to_move = arr[start]
            for j in range(start, len(arr) - i - 1):
                arr[j] = arr[j + 1]
            arr[-i - 1] = item_to_move

    deleted_items = []
    for _ in range(count):
        if arr:
            deleted_items.append(arr.pop())

    for item in reversed(insert_items):
        arr.insert(start, item)

    return deleted_items


a = [1, 2, 3, 4]
b = splice(a, 1, 1)
print(a)  # [1, 3, 4]
print(b)  # [2]

a = [1, 2, 3, 4]
b = splice(a, 1, 2, 5, 6)
print(a)  # [1, 5, 6, 4]
print(b)  # [2, 3]

a = [1, 2, 3, 4]
b = splice(a, 1)
print(a)  # [1]
print(b)  # [2, 3, 4]

a = [1, 2, 3, 4]
b = splice(a, 2, 2, 7, 8, 9)
print(a)  # [1, 2, 7, 8, 9]
print(b)  # [3, 4]
