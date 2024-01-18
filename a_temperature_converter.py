'''
Write a program that takes a temperature value and a scale (Celsius or Fahrenheit) as input
from the user. Convert the temperature to the other scale and print the result.
'''

def celsius_to_fahrenheit(celsius: float) -> float:
    return 9/5 * celsius + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return 5/9 * (fahrenheit - 32)

value = float(input("Value: "))
scale = input("Scale (C or F): ")
print()

if scale == "C" or scale == "c":
    print(f"Celsius: {value}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(value)}")

elif scale == "F" or scale == "f":
    print(f"Fahrenheit: {value}")
    print(f"Celsius: {fahrenheit_to_celsius(value)}")

else:
    print("Invalid scale.")
