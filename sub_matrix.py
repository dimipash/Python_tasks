class Range:
    """
    This class represents a range of integers. It is used to specify a range of rows or columns in a matrix.

    Attributes:
    start (int): The start of the range.
    stop (int): The end of the range.
    """

    def __init__(self, start, stop):
        """
        The constructor for the Range class.

        Parameters:
        start (int): The start of the range.
        stop (int): The end of the range.
        """
        if start >= stop:
            raise ValueError('Start must be before stop')
        if start < 0 or stop < 0:
            raise ValueError('Negative values are not allowed')
        self.start = start
        self.stop = stop + 1


class Matrix:
    """
    This class represents a matrix of numbers. It provides methods to set and get values at specific indices,
    and to get a submatrix within a specified range of rows and columns.

    Attributes:
    cols (int): The number of columns in the matrix.
    rows (int): The number of rows in the matrix.
    data (list of list of int): The data in the matrix.
    """

    def __init__(self, cols, rows, default_value=0):
        """
        The constructor for the Matrix class.

        Parameters:
        cols (int): The number of columns in the matrix.
        rows (int): The number of rows in the matrix.
        default_value (int, optional): The default value for all elements in the matrix. Defaults to 0.
        """
        if cols < 0 or rows < 0:
            raise ValueError("Negative values not allowed")
        self.cols = cols
        self.rows = rows
        self.data = [[default_value for i in range(rows)] for j in range(cols)]

    def check_index(self, x, y):
        """
        This method checks if the given indices are valid for this matrix.

        Parameters:
        x (int): The row index.
        y (int): The column index.

        Raises:
        IndexError: If the indices are not valid.
        """
        if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
            raise IndexError("Not a valid index")

    def set(self, x, y, value):
        """
        This method sets the value at the given indices in the matrix.

        Parameters:
        x (int): The row index.
        y (int): The column index.
        value (int): The value to set.
        """
        self.check_index(x, y)
        self.data[x][y] = value

    def get(self, x, y):
        """
        This method gets the value at the given indices in the matrix.

        Parameters:
        x (int): The row index.
        y (int): The column index.

        Returns:
        int: The value at the given indices.
        """
        self.check_index(x, y)
        return self.data[x][y]

    def subMatrix(self, cols, rows):
        """
        This method gets a submatrix within a specified range of rows and columns.

        Parameters:
        cols (Range): The range of columns.
        rows (Range): The range of rows.

        Returns:
        Matrix: The submatrix.
        """
        if not isinstance(cols, Range) or not isinstance(rows, Range):
            raise TypeError("cols and rows must be of type Range")

        if cols.start < 0 or cols.stop > self.cols or rows.start < 0 or rows.stop > self.rows:
            raise ValueError("Range is out of matrix bounds")

        sub_matrix = Matrix(cols.stop - cols.start, rows.stop - rows.start)

        for i in range(cols.start, cols.stop):
            for j in range(rows.start, rows.stop):
                value = self.data[i][j]
                sub_matrix.data[i - cols.start][j - rows.start] = value

        return sub_matrix

m = Matrix(4, 4)
for i in range(4):
    m.set(i, i, i + 1)

cols = Range(1, 2)
rows = Range(2, 3)
m2 = m.subMatrix(rows, cols)

for row in m2.data:
    print(row)
