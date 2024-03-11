import array


class myarray(array.array):
    """
        This class extends the built-in array class in Python with a modified __setitem__ method.

        The __setitem__ method in this class allows for setting the value of a specific index or slice in the array.
        If the index is a slice, the method converts the value to an array before setting it.
    """
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            value = array.array(self.typecode, value)
        super().__setitem__(index, value)


a = myarray('i', [1, 2, 3, 4])
a[1:2] = [7, 8, 9]
print(a)  # ('i', [1, 7, 8, 9, 3, 4])
