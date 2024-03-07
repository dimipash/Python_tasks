class Matrix:
    """
        This class represents a matrix of numbers.

        Attributes:
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
            val (int): The value to fill the matrix with.
        """

    def __init__(self, rows, cols, val):
        """
            The constructor for the Matrix class.

            Args:
                rows (int): The number of rows in the matrix.
                cols (int): The number of columns in the matrix.
                val (int): The value to fill the matrix with.
            """
        self.rows = rows
        self.cols = cols
        self.val = val

    def __mul__(self, num):
        """
                This method allows for multiplication of the matrix by a number.

                Args:
                    num (int): The number to multiply the matrix by.

                Returns:
                    Matrix: A new Matrix object with the same dimensions as the original, but with all values multiplied by num.
                """
        return Matrix(self.rows, self.cols, self.val * num)

    def __rmul__(self, num):
        """
                This method allows for multiplication of a number by the matrix.

                Args:
                    num (int): The number to multiply the matrix by.

                Returns:
                    Matrix: A new Matrix object with the same dimensions as the original, but with all values multiplied by num.
                """

        return self.__mul__(num)

    def __repr__(self):
        """
                This method returns a string representation of the matrix.

                Returns:
                    str: A string representation of the matrix.
                """
        return '\n'.join([' '.join([str(self.val) for _ in range(self.cols)]) for _ in range(self.rows)])


m = Matrix(2, 2, 3)
print("Original Matrix:")
print(m)
m1 = m * 2
print("Matrix after multiplication with 2:")
print(m1)
m2 = 3 * m
print("Matrix after multiplication with 3:")
print(m2)
