#!/usr/bin/env python3

import time


def get_current_datetime():
    """Return current date and time using manual calculations."""
    now = time.time()          # seconds since epoch (allowed)

    days = int(now // 86400)
    secs = int(now % 86400)

    hour = secs // 3600
    secs %= 3600
    minute = secs // 60
    second = secs % 60

    year = 1970
    days_left = days

    def leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    while True:
        yd = 366 if leap(year) else 365
        if days_left < yd:
            break
        days_left -= yd
        year += 1

    month_days = [31, 29 if leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    month = 1
    for md in month_days:
        if days_left < md:
            break
        days_left -= md
        month += 1

    day = days_left + 1

    # Required formatting: %Y-%m-%d %H:%M:%S
    return f"{year:04d}-{month:02d}-{day:02d} " \
           f"{hour:02d}:{minute:02d}:{second:02d}"


def add_days(year, month, day, extra):
    """Add days manually without datetime module."""

    def leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    month_days = [31, 29 if leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    day += extra

    while True:
        md = month_days[month - 1]
        if day <= md:
            break
        day -= md
        month += 1

        if month > 12:
            month = 1
            year += 1
            month_days = [31, 29 if leap(year) else 28, 31, 30,
                          31, 30, 31, 31, 30, 31, 30, 31]

    return year, month, day


def main():
    current = get_current_datetime()
    print("Current date and time (formatted as %Y-%m-%d %H:%M:%S):")
    print(current)

    # Required input text
    print("Enter the number of days to add to the current date:")
    days_to_add = int(input())

    y, m, d = map(int, current.split()[0].split('-'))
    new_y, new_m, new_d = add_days(y, m, d, days_to_add)

    print(f"New date: {new_y:04d}-{new_m:02d}-{new_d:02d}")


if __name__ == "__main__":
    main()
