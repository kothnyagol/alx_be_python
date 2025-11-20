#!/usr/bin/python3
"""
Temperature Conversion Tool
Converts temperatures between Celsius and Fahrenheit.
Demonstrates the use of global variables.
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_FAHRENHEIT = 32


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global factor
    """
    celsius = (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global factor
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT
    return fahrenheit

def main():
    """
    Main program for user interaction
    """
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # convert string to float
        
        # Ask user for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
