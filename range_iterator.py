class Range:
    """
       This class represents a range of numbers.

       Attributes:
           end (int): The end of the range.
           step (int): The step size for the range.
           x (int): The current value in the range.
    """
    def __init__(self, start, end, step=1):
        """
                The constructor for the Range class.

                Args:
                    start (int): The start of the range.
                    end (int): The end of the range.
                    step (int, optional): The step size for the range. Defaults to 1.
        """
        self.end = end
        self.step = step
        self.x = start - step

    def __next__(self):
        """
               This method returns the next value in the range.

               Returns:
                   int: The next value in the range.

               Raises:
                   StopIteration: If there are no more values in the range.
        """
        self.x += self.step

        if self.x < self.end:
            return self.x

        raise StopIteration

    def __iter__(self):
        """
               This method returns the iterator for the range.

               Returns:
                   Range: The iterator for the range.
        """
        return self


for i in Range(5, 20, 5):
    print(i)
