'''
Create a function that takes a list of numbers as input and returns the sum of all the elements.
'''

def sum_elements() -> int:
    numbers = [float(i) for i in input("Numbers: ").split()]
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(f"Sum: {sum_elements()}")
