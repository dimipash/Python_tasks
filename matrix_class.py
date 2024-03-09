import array


class Matrix:
    """
       This class represents a matrix of numbers.

       Attributes:
           rows (int): The number of rows in the matrix.
           cols (int): The number of columns in the matrix.
           typecode (str): The typecode character used to create the array.
           data (array): The array representing the matrix.
    """

    def __init__(self, rows, cols, initial_value, typecode):
        if rows < 0 or cols < 0:
            raise ValueError("Matrix dimensions must be non-negative")
        if typecode not in array.typecodes:
            raise TypeError('Invalid typecode')
        self.rows = rows
        self.cols = cols
        self.typecode = typecode
        self.data = array.array(typecode, [initial_value] * cols * rows)

    def get_index(self, row, col):
        return row * self.cols + col

    def __getitem__(self, m_index):
        if not isinstance(m_index, tuple):
            raise TypeError("not a tuple")
        row, col = m_index
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            raise IndexError('Matrix index out of range')
        index = self.get_index(row, col)
        return self.data[index]

    def __setitem__(self, m_index, value):
        row, col = m_index
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            raise IndexError('Matrix index out of range')
        index = self.get_index(row, col)
        self.data[index] = value

    def __str__(self):
        return '\n'.join(' '.join(str(self[i, j]) for j in range(self.cols)) for i in range(self.rows))


m = Matrix(12, 5, 0, typecode='H')
m[2, 3] = 1
m[3, 2] = 3
print(m[2, 3], m[3, 2])
