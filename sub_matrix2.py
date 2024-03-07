class Matrix:
    """
    This class represents a matrix of numbers.

    Attributes:
        data (list of lists): A 2D list representing the matrix.
    """

    def __init__(self, rows, cols):
        """
        The constructor for the Matrix class.

        Args:
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
        """
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def submatrix(self, row_indexes, col_indexes):
        """
        This method returns a submatrix specified by the given row and column indexes.

        Args:
            row_indexes (range, slice, list, tuple): The indexes of the rows to be included in the submatrix.
            col_indexes (range, slice, list, tuple): The indexes of the columns to be included in the submatrix.

        Returns:
            list of lists: The submatrix as a 2D list.
        """
        row_indexes = self._convert_to_range(row_indexes)
        col_indexes = self._convert_to_range(col_indexes)

        return [[self.data[row][col] for col in col_indexes] for row in row_indexes]

    def _convert_to_range(self, indexes):
        """
        This private method converts various types of indexes to a range.

        Args:
            indexes (range, slice, list, tuple): The indexes to be converted.

        Returns:
            range: The indexes as a range.

        Raises:
            TypeError: If the type of indexes is not supported.
        """
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
