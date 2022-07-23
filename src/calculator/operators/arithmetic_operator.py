'''This module contains the basic arithmetic operators.'''


class ArithmeticOperator:
    '''This class is the base class for the basic operators.
    It stores the first and second arguments, as well as the result. These
    will be used when the operation is retrieved from the history stack.'''

    def __init__(self, **kwargs):
        self.args = kwargs['args']
        self.result = None

    def __call__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    @classmethod
    def desc(cls):
        '''Returns the description of the operator.'''

        raise NotImplementedError


class Add(ArithmeticOperator):
    '''This class implements the Add operation.'''

    def __call__(self):
        self.result = self.args[0] + self.args[1]
        return self.result

    def __str__(self):
        return f"{self.args[0]} + {self.args[1]} = {self.result}"

    @classmethod
    def desc(cls):
        return "Arithmetic addition"


class Subtract(ArithmeticOperator):
    '''This class implements the Subtract operation.'''

    def __call__(self):
        self.result = self.args[0] - self.args[1]
        return self.result

    def __str__(self):
        return f"{self.args[0]} - {self.args[1]} = {self.result}"

    @classmethod
    def desc(cls):
        return "Arithmetic subtraction"


class Multiply(ArithmeticOperator):
    '''This class implements the Multiply operation.'''

    def __call__(self):
        self.result = self.args[0] * self.args[1]
        return self.result

    def __str__(self):
        return f"{self.args[0]} * {self.args[1]} = {self.result}"

    @classmethod
    def desc(cls):
        return "Arithmetic multiplication"


class Divide(ArithmeticOperator):
    '''This class implements the Divide operation.'''

    def __call__(self):
        if self.args[1] == 0:
            if self.args[0] < 0:
                self.result = float("-inf")
            else:
                self.result = float("inf")
        else:
            self.result = self.args[0] / self.args[1]
        return self.result

    def __str__(self):
        return f"{self.args[0]} / {self.args[1]} = {self.result}"

    @classmethod
    def desc(cls):
        return "Arithmetic division"
