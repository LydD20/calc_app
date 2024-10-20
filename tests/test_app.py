'''docstring for pylint'''
import os
import pytest
from calculator.commands.app import App  # Import the App class

@pytest.fixture(autouse=True)
def set_test_env():
    '''Set up testing environment'''
    # Mock the ENVIRONMENT variable for the test
    os.environ['ENVIRONMENT'] = 'TESTING'

def test_app_get_environment_variable():
    """Test to ensure environment variable retrieval works correctly."""
    app = App()
    # Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

# Apply the parametrize decorator to the test function
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_print method for various operations and scenarios."""
    app = App()
    # Call the calculate_and_print method
    app.calculate_and_print(a_string, b_string, operation_string)
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the output matches the expected string
    assert captured.out.strip() == expected_string
