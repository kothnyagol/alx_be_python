#!/usr/bin/env python3

def get_current_datetime():
    """Return current date and time (no datetime module)."""
    import time

    now = time.time()          # seconds since Jan 1, 1970
    days = int(now // 86400)   # number of full days since epoch
    seconds = int(now % 86400)

    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60

    # Calculate a readable date starting from 1970
    year = 1970
    days_left = days

    # Helper function
    def leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    # Deduct years
    while True:
        year_days = 366 if leap(year) else 365
        if days_left < year_days:
            break
        days_left -= year_days
        year += 1

    # Deduct months
    month_days = [31, 29 if leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    month = 1
    for md in month_days:
        if days_left < md:
            break
        days_left -= md
        month += 1

    day = days_left + 1

    # Return formatted date-time string
    return f"{year:04d}-{month:02d}-{day:02d} " \
           f"{hour:02d}:{minute:02d}:{second:02d}"


def add_days(year, month, day, extra_days):
    """Return a new Y-M-D after adding days (manual calculation)."""

    def leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    month_days = [31, 29 if leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    day += extra_days

    while True:
        md = month_days[month - 1]
        if day <= md:
            break
        day -= md
        month += 1
        if month > 12:
            month = 1
            year += 1
            month_days = [31, 29 if leap(year) else 28, 31, 30, 31,
                          30, 31, 31, 30, 31, 30, 31]

    return year, month, day


def main():
    current = get_current_datetime()
    print("Current date and time (YYYY-MM-DD HH:MM:SS):")
    print(current)

    print("Enter the number of days to add to the current date:")
    days_to_add = int(input())

    y, m, d = map(int, current.split()[0].split('-'))
    new_y, new_m, new_d = add_days(y, m, d, days_to_add)

    formatted_new = f"{new_y:04d}-{new_m:02d}-{new_d:02d}"
    print("New date after adding days:", formatted_new)


if __name__ == "__main__":
    main()
