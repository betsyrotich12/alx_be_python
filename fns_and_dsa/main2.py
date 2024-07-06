from temp_conversion_tool import *
def main():
    try:
        temperature = float(input("Enter the temperature to convert:"))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    unit = input("Is this temperature in Celsius or Farenheit? (C/F):")

    match unit:
        case "F":
            converted_temperature = convert_to_celsius(temperature)
            print(temperature, " °F is", converted_temperature, "°C")

        case "C":
            converted_temperature = convert_to_fahrenheit(temperature)
            print(unit, " °C is", converted_temperature, "°F")

        case _:
            print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
