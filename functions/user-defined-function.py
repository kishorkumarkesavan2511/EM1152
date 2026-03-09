def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero is undefined"

while True:
    ch = input("Menu:1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit \nEnter your choice (1-5): ")
    if ch in ['1', '2', '3', '4']:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        
        op = {
            '1': add(a, b),
            '2': subtract(a, b),
            '3': multiply(a, b),
            '4': divide(a, b)
        }
        
        print(f"The result is: {op[ch]}")
    elif ch== '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
