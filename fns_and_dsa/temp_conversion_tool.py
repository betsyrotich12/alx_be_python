FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
try:
    temperature = float(input("Enter the temperature to convert:"))
except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    farenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return farenheit

    