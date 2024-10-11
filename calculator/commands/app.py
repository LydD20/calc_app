from calculator.plugins.addition.add_plugin import AddCommand
from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand
from decimal import Decimal, InvalidOperation

# Initialize history list to store calculation history
history = []

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand,
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command_class = operation_mappings.get(operation_name)

        if command_class:
            command = command_class(a_decimal, b_decimal)
            result = command.execute()

            # Append result to history
            history.append(f"{a} {operation_name} {b} = {result}")
            print(f"The result of {a} {operation_name} {b} is equal to {result}")  # Updated output
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")  # This part is fine
    except Exception as e:
        print(f"An error occurred: {e}")

def show_history():
    """Display the history of calculations."""
    if not history:
        print("No history available.")
    else:
        print("Calculation History:")
        for entry in history:
            print(entry)

def main():
    print("Welcome to the Command-based Calculator!")
    
    while True:
        command = input("Enter 'c' to perform a calculation, 'h' to view history, or 'q' to quit: ").strip().lower()
        
        if command == 'c':
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
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