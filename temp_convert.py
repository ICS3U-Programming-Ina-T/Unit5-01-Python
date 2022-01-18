#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 17, 2021
# This program converts the entered temperature
# in Celcius to Fahrenheit.


def calculate_fahrenheit():

    # gets temperature from the user
    temp_c_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # converts string to float
        temp_c_float = float(temp_c_string)
        # calculates the fahrenheit
        temp_f = (9/5) * temp_c_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F" .format(temp_c_float, temp_f))

    # checks if the number is a string
    except Exception:
        print("{} is not a number.". format(temp_c_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
