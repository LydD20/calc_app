'''Testing Commands'''

from decimal import Decimal
import pytest
from calculator.plugins.add.add_plugin import AddCommand
from calculator.plugins.divide.divide_plugin import DivideCommand

#add command
def test_add_command():
    command = AddCommand(Decimal('3'), Decimal('5'))
    assert command.execute() == Decimal('8')

#divide command
def test_divide_command():
    command = DivideCommand(Decimal('10'), Decimal('2'))
    assert command.execute() == Decimal('5')

#divide command error
def test_divide_by_zero():
    command = DivideCommand(Decimal('10'), Decimal('0'))
    with pytest.raises(ZeroDivisionError, match="An error occurred: Cannot divide by zero"):
        command.execute()
        