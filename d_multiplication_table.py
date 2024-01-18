'''
Write a program that takes a number as input from the user and prints its multiplication
table up to 10.
'''

n = int(input("Number: "))
print()

for i in range(10):
    print(f"{n} x {i+1:2} = {n*(i+1)}")
