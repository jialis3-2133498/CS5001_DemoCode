def main():
    BASE = 32
    CONVERSION_FACTOR = 5.0/9.0
    TEMP_PRECISION = 2

    # Get input from user
    fahrenheit_temp = float(input("Input a temperature in Fahrenheit: "))

    celsius_temp = (fahrenheit_temp - BASE) * CONVERSION_FACTOR

    print(f"Result: {round(celsius_temp, TEMP_PRECISION)} degrees celsius")


main()
