class Fib:
    """
        This class represents a Fibonacci sequence up to a given number of terms.

        Attributes:
            n (int): The number of terms in the sequence.
            first (int): The first term in the sequence.
            second (int): The second term in the sequence.
            counter (int): The current term in the sequence.
    """

    def __init__(self, n):
        self.n = n
        self.first = 0
        self.second = 1
        self.counter = 0

    def __next__(self):
        if self.counter >= self.n:
            raise StopIteration

        x = self.first
        self.first = self.second
        self.second += x
        self.counter += 1
        return x

    def __iter__(self):
        return self


for i in Fib(6):
    print(i)
