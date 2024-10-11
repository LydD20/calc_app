'''Test for Calculation class and Calculator operations'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide

def test_calculation_operations(a, b, operation, expected):
     #Test calculation operations with different cases.

    calc = Calculation(a, b, operation) 
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}" 

def test_calculation_repr():
    #test for string representation 
    
    calc = Calculation(Decimal('10'), Decimal('5'), add) 
    expected_repr = "Calculation(10, 5, add)" 
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    #test division by zero to check it causes a ValueErrorTest division by zero to ensure it raises a ValueError.

    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()  