class Matrix:
    """
    This class represents a matrix of numbers. It provides methods to set and get values at specific indices.

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

m = Matrix(2, 2, -1)
m.set(0, 1, 15)
v1 = m.get(0, 1)
v2 = m.get(0, 0)
print(v1, v2)  # Output: 15 -1
