'''This module contains the basic arithmetic operators.'''


class ArithmeticOperator:
    '''This class is the base class for the basic operators.
    It stores the first and second arguments, as well as the result. These
    will be used when the operation is retrieved from the history stack.'''

    def __init__(self, **kwargs):
        self.first = kwargs['first']
        self.second = kwargs['second']
        self.result = None

    def __call__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Add(ArithmeticOperator):
    '''This class implements the Add operation.'''

    def __call__(self):
        self.result = self.first + self.second
        return self.result

    def __str__(self):
        return f"{self.first} + {self.second} = {self.result}"


class Subtract(ArithmeticOperator):
    '''This class implements the Subtract operation.'''

    def __call__(self):
        self.result = self.first - self.second
        return self.result

    def __str__(self):
        return f"{self.first} - {self.second} = {self.result}"


class Multiply(ArithmeticOperator):
    '''This class implements the Multiply operation.'''

    def __call__(self):
        self.result = self.first * self.second
        return self.result

    def __str__(self):
        return f"{self.first} * {self.second} = {self.result}"


class Divide(ArithmeticOperator):
    '''This class implements the Divide operation.'''

    def __call__(self):
        self.result = self.first / self.second
        return self.result

    def __str__(self):
        return f"{self.first} / {self.second} = {self.result}"
