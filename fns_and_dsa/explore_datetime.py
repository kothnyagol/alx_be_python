#!/usr/bin/python3
from datetime import datetime, timedelta


def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()

    year = current_date.year
    month = current_date.month
    day = current_date.day
    hour = current_date.hour
    minute = current_date.minute
    second = current_date.second

    formatted_date = (
        f"{year}-{month:02d}-{day:02d} "
        f"{hour:02d}:{minute:02d}:{second:02d}"
    )

    print("Current date and time:", formatted_date)
    return current_date


def calculate_future_date(current_date, days_to_add):
    """Calculate date after adding given number of days."""
    future_date = current_date + timedelta(days=days_to_add)

    year = future_date.year
    month = future_date.month
    day = future_date.day

    formatted_future = (
        f"{year}-{month:02d}-{day:02d}"
    )

    print("Future date:", formatted_future)
    return future_date


if __name__ == "__main__":
    current = display_current_datetime()

    days = int(input("Enter the number of days to add: "))
    calculate_future_date(current, days)
