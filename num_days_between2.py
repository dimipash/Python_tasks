def days_since_start_of_year(date):
    year, month, day = [int(x) for x in date.split("-")]
    days_in_month = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day + sum(days_in_month[:month - 1])


def num_days_between(date1, date2):
    if date1.split("-")[2] != date2.split("-")[2]:
        return None
    return abs(days_since_start_of_year(date1) - days_since_start_of_year(date2))


print(num_days_between("11-06-2021", "12-06-2021"))
print(num_days_between("1-01-2021", "1-02-2021"))