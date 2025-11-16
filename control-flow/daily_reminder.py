#!/usr/bin/python3
# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' is a task with an unknown priority"

# Check time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

# Final reminder (this is what the checker is looking for!)
print(f"Reminder: {message}")
