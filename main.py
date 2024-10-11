import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

# Initialize an empty history list
history = []

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide,
        'exponent': Calculator.exponent,
        'radical_expression': Calculator.radical_expression,
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result_function = operation_mappings.get(operation_name)
        if result_function:
            calculation_result = result_function(a_decimal, b_decimal)
            history.append(f"{a} {operation_name} {b} = {calculation_result}")
            print(f"The result of {a} {operation_name} {b} is equal to {calculation_result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_history():
    """Display the history of calculations."""
    if not history:
        print("No history available.")
        return
    print("Calculation History:")
    for entry in history:
        print(entry)

def main():
    print("Welcome to the Calculator!")
    while True:
        command = input("Enter 'c' to perform a calculation, 'h' to view history, or 'q' to quit: ").strip().lower()
        
        if command == 'c':
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            operation = input("Enter the operation (add, subtract, multiply, divide, exponent, radical_expression): ").strip().lower()
            calculate_and_print(a, b, operation)
        
        elif command == 'h':
            show_history()

        elif command == 'q':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()