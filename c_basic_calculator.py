def menu() -> int:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    return int(input("Response: "))

a = float(input("Operator A: "))
b = float(input("Operator B: "))
print()

result = 0
response = menu()
print()

if response == 1:
    result = a + b

elif response == 2:
    result = a - b

elif response == 3:
    result = a * b

elif response == 4:
    result = a / b

print(f"Result: {result}")
