"""
This class implements a moving average filter. It keeps track of the last `n` numbers and
calculates the average of those numbers.

Args:
   n: An integer specifying the number of elements to store in the moving window.

Raises:
   TypeError: If `n` is not an integer.
   ValueError: If `n` is less than or equal to zero.
"""


class Average:
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError('n must be an integer')
        if n <= 0:
            raise ValueError('n must be greater than 0')
        self.n = n
        self.num_list = []

    def next(self, num):
        if not isinstance(num, (float, int)):
            raise TypeError('num must be a number')

        self.num_list.append(num)
        if len(self.num_list) > self.n:
            self.num_list.pop(0)

        return sum(self.num_list) / len(self.num_list)


avg = Average(3)

val = avg.next(1)
print(val)  # 1.0
val = avg.next(2)
print(val)  # 1.5
val = avg.next(3)
print(val)  # 2.0
val = avg.next(4)
print(val)  # 3.0
val = avg.next(5)
print(val)  # 4.0
val = avg.next(0)
print(val)  # 3.0
