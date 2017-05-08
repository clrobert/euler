"""
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""


def num_days_in_year(year):
    default = 365
    leap = default + 1
    days = 0

    if is_leap_year(year):
        days = leap
    else:
        days = default
    return days


def is_leap_year(year):
    default = False
    leap = True

    if year % 400 == 0:
        days = leap
    elif year % 100 == 0:
        days = default
    elif year % 4 == 0:
        days = leap
    else:
        days = default
    return days


def is_first_of_month(day, is_leap_year):
    """Given an integer 1-366, returns whether or not
    that given int is the first of the month in a given year.
    """

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]

    if is_leap_year:
        months[2] += 1

    total = 0
    month = 0
    while(day >= total):
        total = total + months[month]
        month = month + 1

    if day == total - months[month - 1] + 1 or day == 1:
        return True
    else:
        return False


def is_sunday(day):
    return day % 7 + 1 == 7


def num_sundays():
    offset = 0
    sundays = 0
    for year in range(1901, 2001):
        num_days = num_days_in_year(year)

        for day in range(1, num_days + 1):
            if is_sunday(day + offset):
                if is_first_of_month(day, is_leap_year(year)):
                    sundays += 1

        offset = (offset + num_days) % 7
    return sundays

print(num_sundays())
