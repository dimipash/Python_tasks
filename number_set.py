"""
    The NumberSet class represents a set of numbers between 0 and 100.
    It has a constructor that initializes an array of boolean values
    representing the presence of numbers in the set. It has an add 
    method that adds a number to the set, a remove method that
    removes a number from the set, and a contains method that 
    checks if a number is in the set. It also has a _validate 
    method that validates a number. The _validate method is
    called by the add, remove, and contains methods to ensure
    that the number is between 0 and 100. If the number is not
    between 0 and 100, the _validate method raises a ValueError.
    This class does not check the types of the arguments, so
    you should ensure they are integers before using this
    class. If they are not, this class may raise a TypeError.
"""

class NumberSet:
    def __init__(self):
        self.array = [False] * 101

    def add(self, number):
        self._validate(number)
        self.array[number] = True

    def remove(self, number):
        self._validate(number)
        self.array[number] = False

    def contains(self, number):
        self._validate(number)
        return self.array[number]

    def _validate(self, number):
        if not 0 <= number <= 100:
            raise ValueError("Number must be between 0 and 100")


numbers = NumberSet()
numbers.add(3)
print(numbers.contains(3))  # Output: True
numbers.remove(7)
print(numbers.contains(7))  # Output: False
