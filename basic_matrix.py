"""
This class implements a basic matrix data structure and provides a method to extract submatrices.

Attributes:
    data (list): A 2D list representing the matrix data.

Methods:
    submatrix(self, row_indexes, col_indexes):
        Extracts a submatrix from the main matrix based on the provided row and column indices.

Raises:
    TypeError: If the provided row or column indices are not of a supported type
               (range, slice, list, or tuple).
"""


class Matrix:

    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def submatrix(self, row_indexes, col_indexes):
        row_indexes = self._convert_to_range(row_indexes)
        col_indexes = self._convert_to_range(col_indexes)

        return [[self.data[row][col] for col in col_indexes] for row in row_indexes]

    def _convert_to_range(self, indexes):
        if isinstance(indexes, range):
            return indexes
        if isinstance(indexes, slice):
            return range(indexes.start, indexes.stop)
        if isinstance(indexes, list):
            return range(indexes[0], indexes[1])
        if isinstance(indexes, tuple):
            start, stop = indexes
            return range(start, stop)

        raise TypeError('Unsupported index type', type(indexes))


m = Matrix(5, 5)
m1 = m.submatrix([0, 3], [2, 4])
m2 = m.submatrix((1, 3), (2, 4))
m3 = m.submatrix(slice(1, 3), slice(2, 4))
m4 = m.submatrix(range(1, 3), range(2, 4))
m5 = m.submatrix(slice(1, 3), [2, 4])
m6 = m.submatrix((1, 3), range(2, 4))
print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
