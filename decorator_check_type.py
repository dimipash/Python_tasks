"""
The accepts function is a decorator that checks if the arguments of the decorated function are of the correct types.
It takes any number of type arguments and checks the arguments of the decorated function against these types. If
an argument is not of the correct type, it raises a TypeError.bThe returns function is a decorator that checks if 
the return value of the decorated function is of the correct type.vIt takes a single type argument and checks the 
return value of the decorated function against this type. If thereturn value is not of the correct type, it raises
 a TypeError. The bar function calculates the average of two numbers. It takes two integer arguments and returns
their average as a float. This function is decorated with the accepts and returns decorators to enforce type checking 
on its arguments and return value.
"""

def accepts(*types):
    for t in types:
        if not isinstance(t, type):
            raise TypeError(f"{t} is not of type {type(t)}")

    def inner(func):
        def call(*args):
            for type, arg in zip(types, args):
                if not isinstance(arg, type):
                    raise TypeError("Argument is not of type")

            return func(*args)

        return call

    return inner


def returns(return_type):
    if not isinstance(return_type, type):
        raise TypeError(f"{return_type} is not of type")

    def inner(func):
        def call(*args):
            result = func(*args)

            if not isinstance(result, return_type):
                raise TypeError(f"Result with type {return_type} is not of type")

            return result

        return call

    return inner


@accepts(int, int)
@returns(float)
def bar(low, high):
    return (low + high) / 2


print(bar(10, 20))
