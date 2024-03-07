def custom_range(start, stop, step):
    """
    This function generates a list of numbers, starting from 'start', ending before 'stop', and incrementing by 'step'.

    Args:
        start (int): The number at which to start the range.
        stop (int): The function will generate numbers up to, but not including, this number.
        step (int): The difference between each number in the range.

    Returns:
        list: Returns a list of numbers in the specified range with the specified step.
    """
    numbers = []
    i = start
    while i < stop:
        numbers.append(i)
        i += step
    return numbers


for i in custom_range(2, 10, 3):
    print(i)
