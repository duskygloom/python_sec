'''
Create a program that prompts the user to enter a number and then calculates and prints its
factorial using a while loop.
'''

def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

n = int(input("Number: "))
print(f"{n}! = {factorial(n)}")
