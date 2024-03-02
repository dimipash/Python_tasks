list_1 = [1, 2, 3]

generator = (list_1[n] for n in range(len(list_1) - 1, -1, -1))

for i in generator:
    print(i)
