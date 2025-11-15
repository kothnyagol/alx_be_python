#!/usr/bin/python3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is {result}")
else:
    print("Invalid operation selected.")
