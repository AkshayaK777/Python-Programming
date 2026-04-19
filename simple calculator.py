def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    a = float(input("Enter first number: "))
    op = input("Enter operation: ")
    b = float(input("Enter second number: "))

    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    if op in ops:
        print(f"Result: {ops[op](a, b)}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()