from calculator.plugins.addition.add_plugin import AddCommand
from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
import logging
import logging.config
import os


class App:
    def __init__(self):
        #Create logs directory 
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()  # Configures logging
        self.load_environment_variables()  # Loads Environmental Variables
        
        #Load env variables or use the default 'PRODUCE'
        environment = os.getenv("ENVIRONMENT")
        if not environment:  # Check if ENVIRONMENT is not set
            load_dotenv() 
            environment = os.getenv("ENVIRONMENT", 'PRODUCE')  # Default to 'PRODUCE'
        #Store env variable in settings
        self.settings = {
            'ENVIRONMENT': environment  #
        }

        #Initialize history list
        self.history = []

    def load_environment_variables(self):
        return {
            'ENVIRONMENT': os.getenv('ENVIRONMENT')
        }

    def get_environment_variable(self, var_name):
        return self.settings.get(var_name)

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                filename='logs/app.log',  #Log to file in  logs directory
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Logging is set up.")

    def calculate_and_print(self, a, b, operation_name):
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

                #Add result to history
                self.history.append(f"{a} {operation_name} {b} = {result}")
                print(f"The result of {a} {operation_name} {b} is equal to {result}")  #Updated output
                logging.info(f"Calculated: {a} {operation_name} {b} = {result}")  #Log calculation
            else:
                print(f"Unknown operation: {operation_name}")
                logging.warning(f"Unknown operation attempted: {operation_name}")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
            logging.error(f"Invalid number input: {a} or {b} is not a valid number.")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero") 
            logging.error("Division by zero attempted.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"An error occurred: {e}")

    def show_history(self):
        """Display the history of calculations."""
        if not self.history:
            print("No history available.")
        else:
            print("Calculation History:")
            for entry in self.history:
                print(entry)
            logging.info("Displayed calculation history.")

    def main(self):
        print("Welcome to the Command-based Calculator!")
        
        while True:
            command = input("Enter 'c' to perform a calculation, 'h' to view history, or 'q' to quit: ").strip().lower()
            
            if command == 'c':
                operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                self.calculate_and_print(a, b, operation)
            
            elif command == 'h':
                self.show_history()
                logging.info("Calculator History entered.")

            elif command == 'q':
                print("Exiting the calculator.")
                logging.info("Calculator exited.")
                break
            
            else:
                print("Invalid command. Please try again.")

if __name__ == '__main__':
    app = App() 
    app.main()  #Start the main application loop
