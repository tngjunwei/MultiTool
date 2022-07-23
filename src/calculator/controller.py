'''This module contains the controller class for the Calculator application.'''

from .operators import operator_map


class CalculatorController:
    '''This class handles the execution of the operators from the inputs
     (from CLI or requests).'''

    def __init__(self):
        self.operators = operator_map

    def get_operators(self):
        '''Returns the dictionary of operators.'''

        return self.operators

    def execute(self, op_lbl, args):
        '''Executes the operator with arguments and returns the operator
         object.'''

        operator = self.operators[op_lbl]
        do_operation = operator(args=args)
        do_operation()
        return do_operation
