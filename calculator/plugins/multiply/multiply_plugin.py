'''multiply command Imports Command from calculator.commands.command'''
from calculator.commands.command import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b

# def register():
#     return MultiplyCommand