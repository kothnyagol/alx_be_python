#!/usr/bin/python3
"""
A script to explore Python's datetime module.
Performs:
1. Display current date & time
2. Calculate a future date using timedelta
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Displays current date and time
    """
    current_date = datetime.now()  # store current datetime
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """
    Calculates future date from user input
    Args:
        days (int): Number of days to add
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # calculate future
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


if __name__ == "__main__":
    display_current_datetime()

    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Error: Please enter a valid integer for days.")
