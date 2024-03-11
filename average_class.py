"""
    This class calculates the moving average of the last 'n' numbers.
    It maintains a window of the last 'n' numbers and updates the
    window and the sum of the numbers in the window each time a new
    number is added. The average is then calculated as the sum
    divided by the number of numbers in the window.
"""


class Average:
    def __init__(self, n):
        self.n = n
        self.window = []
        self.sum = 0

    def next(self, num):
        if len(self.window) == self.n:
            self.sum -= self.window.pop(0)
        self.window.append(num)
        self.sum += num
        return self.sum / len(self.window)


avg = Average(3)

val = avg.next(1)
print(val)  # 1
val = avg.next(2)
print(val)  # 1.5
val = avg.next(3)
print(val)  # 2
val = avg.next(4)
print(val)  # 3
val = avg.next(5)
print(val)  # 4
val = avg.next(0)
print(val)  # 3
