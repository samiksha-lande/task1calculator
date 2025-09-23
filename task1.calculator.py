# calculator.py
# A simple command-line calculator supporting +, -, *, /

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    print("=== Simple CLI Calculator ===")
    print("Available operations: +  -  *  /")
    
    while True:
        print("\nSelect operation or type 'exit' to quit:")
        operation = input("Enter (+, -, *, /) or exit: ").strip()
        
        if operation.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation! Please choose +, -, *, /")
            continue

        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
