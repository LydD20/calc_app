'''Module for History of Calculations'''
from calculator.calculation import Calculation

class History:
    history = []

    @staticmethod
    def add_calculation(calculation: Calculation):
        #Add a calculation to the history.
        History.history.append(calculation)

    @staticmethod
    def get_history():
        #Return the full history.
        return History.history

    @staticmethod
    def clear_history():
        ##Clear the history.
        History.history.clear()

    @staticmethod
    def get_latest():
        ##Return the latest calculation.
        return History.history[-1] if History.history else None