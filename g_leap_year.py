'''
Write a function called is ‘leap’ year that takes a year as an argument and returns True if it’s
a leap year and False otherwise.
'''

def leap(year: int) -> bool:
    return (year%4 == 0) and not (year%100 == 0 and year%400 != 0)

year = int(input("Year: "))
if leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
