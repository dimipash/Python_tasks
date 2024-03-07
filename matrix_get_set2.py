class Matrix:
    """
        This class represents a matrix of numbers.

        Attributes:
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
            data (list of lists): A 2D list representing the matrix.
        """

    def __init__(self, rows, cols):
        """
               The constructor for the Matrix class.

               Args:
                   rows (int): The number of rows in the matrix.
                   cols (int): The number of columns in the matrix.
               """
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __getitem__(self, index):
        """
             This method allows for indexing and slicing of the matrix.

             Args:
                 index (int, tuple): The index or slice for the row and column.

             Returns:
                 list: The row or submatrix specified by the index or slice.
             """
        if isinstance(index, int):
            return self.data[index]
        if isinstance(index, tuple):
            row_slice, col_slice = index
            if row_slice == ...:
                row_slice = slice(None)
            if col_slice == ...:
                col_slice = slice(None)
            return [row[col_slice] for row in self.data[row_slice]]

    def __setitem__(self, index, value):
        """
               This method allows for setting the value of a specific cell in the matrix.

               Args:
                   index (tuple): The index for the row and column.
                   value (int): The value to set.
               """
        row, col = index
        self.data[row][col] = value


m = Matrix(5, 5)

m1 = m[1]
m2 = m[:, 3]
m3 = m[1:3, 2:4]
m4 = m[..., 2:4]
m5 = m[2:4, :]

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
