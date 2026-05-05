def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("=" * 30)
    print("   Simple CLI Calculator")
    print("=" * 30)
    print("Operations: + | - | * | /")
    print("Type 'quit' to exit\n")

    while True:
        num1 = input("Enter first number: ")
        if num1 == 'quit': break

        op = input("Enter operation (+, -, *, /): ")
        if op == 'quit': break

        num2 = input("Enter second number: ")
        if num2 == 'quit': break

        num1, num2 = float(num1), float(num2)

        if op == '+': result = add(num1, num2)
        elif op == '-': result = subtract(num1, num2)
        elif op == '*': result = multiply(num1, num2)
        elif op == '/': result = divide(num1, num2)
        else:
            print("Invalid operation!\n")
            continue

        print(f"Result: {num1} {op} {num2} = {result}\n")

calculator()