class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, indexes):
        row, col = indexes
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of bounds")

        return self.data[row][col]

    def __setitem__(self, indexes, value):
        row, col = indexes
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of bounds")

        self.data[row][col] = value


m = Matrix(5, 5)
m[4, 1] = 3
b = m[4, 1]
print(b)
m[2, 3] = 5
v = m[2, 3]
print(v)
