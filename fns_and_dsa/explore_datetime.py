#!/usr/bin/python3
from datetime import datetime, timedelta


def display_current_datetime():
    """Display the current date and time using strftime."""
    current_date = datetime.now()

    # ALX checker requires this exact format: %Y-%m-%d %H:%M:%S
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted_date)
    return current_date


def calculate_future_date(current_date, days_to_add):
    """Calculate date after adding given number of days."""
    future_date = current_date + timedelta(days=days_to_add)

    formatted_future = future_date.strftime("%Y-%m-%d")

    print("Future date:", formatted_future)
    return future_date


if __name__ == "__main__":
    current = display_current_datetime()

    days = int(input("Enter the number of days to add: "))
    calculate_future_date(current, days)
