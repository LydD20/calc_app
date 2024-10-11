'''subtract command Imports Command from calculator.commands.command'''
from calculator.commands.command import Command

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

# def register():
#     return SubtractCommand