''' Contains the base Command class'''
class Command:
    def __init__(self, a, b):
        '''init'''
        self.a = a
        self.b = b

    def execute(self):
        '''execute '''
        raise NotImplementedError("Subclasses should implement this method.")