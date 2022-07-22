'''This module registers the operators to their labels.'''

from .arithmetic_operator import Add, Subtract, Multiply, Divide

# Register the operator and their names here

operator_map = {
    "ADD": Add,
    "SUBTRACT": Subtract,
    "MULTIPLY": Multiply,
    "DIVIDE": Divide,
}
