'''This module contains helper functions useful for checking numeric
 strings.'''


def is_integer(number: str):
    '''Checks if the numeric string is an integer or not.'''

    return number.lstrip('-').isnumeric()


def is_float(number: str):
    '''Checks if the numeric string is a float or not. If the string contains
     only 1 decimal point, then it is a float.'''

    return len(number.split('.')) == 2


def is_number(num_str: str):
    '''A helper function for checking numbers. A number is either an integer
     or a float.'''

    return is_integer(num_str) or is_float(num_str)
