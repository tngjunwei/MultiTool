from .base_operator import ArithmeticOperator

class Add(ArithmeticOperator):    
    def __call__(self):
        self.result = self.first + self.second
        return self.result


class Subtract(ArithmeticOperator):
    def __call__(self):
        self.result = self.first - self.second
        return self.result


class Multiply(ArithmeticOperator):
    def __call__(self):
        self.result = self.first * self.second
        return self.result


class Divide(ArithmeticOperator):
    def __call__(self):
        self.result = self.first / self.second
        return self.result
