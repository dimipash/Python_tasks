MAX_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """
        This function checks if a year is a leap year.

        Args:
            year (int): The year to check.

        Returns:
            bool: Returns True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_date(date_str):
    """
        This function validates a date string.

        Args:
            date_str (str): The date string to validate in the format 'dd-mm-yyyy'.

        Returns:
            bool: Returns True if the date string is valid, False otherwise.
    """
    d, m, y = date_str.split('-')

    try:
        day = int(d)
        month = int(m)
        year = int(y)
    except ValueError:
        return False

    if month < 1 or month > 12 or day < 1:
        return False

    MAX_DAYS[1] = 29 if is_leap(year) and month == 2 else 28

    if day > MAX_DAYS[month - 1]:
        return False

    return True


def day_of_week(date_str):
    """
        This function calculates the day of the week for a given date.

        Args:
            date_str (str): The date string in the format 'dd-mm-yyyy'.

        Returns:
            int: Returns the day of the week as an integer (0 for Monday, 1 for Tuesday, ..., 6 for Sunday), or None if the date string is invalid.
    """
    if validate_date(date_str):
        d, m, y = map(int, date_str.split('-'))

        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        after_feb = int(m > 2 and is_leap(y))

        return (d + months[m - 1] + y + int(y / 4)
                - int(y / 100) + int(y / 400) + after_feb - 1) % 7

    else:
        return None


print(day_of_week("30-11-2021"))  # Output: 2

