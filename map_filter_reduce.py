from collections.abc import Iterable
import types


def new_map(func, iterable):
    if not isinstance(iterable, Iterable):
        raise TypeError('Parameter iterable is not iterable')
    if not isinstance(func, types.FunctionType):
        raise TypeError('Parameter func is not a function')

    return [func(i) for i in iterable]


print(new_map(lambda x: x * 2, [1, 2, 3, 4]))  # Output: [2, 4, 6, 8]


def new_filter(func, input):
    if not isinstance(input, Iterable):
        raise TypeError('Parameter iterable is not iterable')
    if not isinstance(func, types.FunctionType):
        raise TypeError('Parameter func is not a function')

    return [n for n in input if func(n)]


print(new_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # Output: [2, 4]


def new_reduce(func, input, initial=None):
    if not isinstance(input, Iterable):
        raise TypeError('Parameter iterable is not iterable')
    if not isinstance(func, types.FunctionType):
        raise TypeError('Parameter func is not a function')

    iterator = iter(input)
    if initial is None:
        initial = next(iterator)

    result = initial
    for el in iterator:
        result = func(result, el)

    return result


print(new_reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # Output: 24
