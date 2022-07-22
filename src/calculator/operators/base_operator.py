class ArithmeticOperator:
    def __init__(self, **kwargs):
        self.first = kwargs['first']
        self.second = kwargs['second']

    def __call__(self):
        raise NotImplementedError