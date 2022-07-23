'''This module contains the command line interface for the Calculator
 application.'''

from src.util.math_util import is_number, is_integer
from .controller import CalculatorController
from .menu import OperatorMenu


class CalculatorCLI:
    '''The command line interface for the Calculator application.'''

    def __init__(self):
        self.controller = CalculatorController()
        self.menu = OperatorMenu(self.controller.get_operators())

    @classmethod
    def desc(cls):
        '''Returns the description of the application.'''

        return 'Calculator App'

    def run(self):
        '''Runs the CLI for the Calculator app.'''
        while True:
            self._print_menu()
            result = self._get_and_exec_input()

            if result is None:
                self._print_exit_msg()
                return
            print(f"Result: {result}\n")

    def _print_menu(self):
        print(self.menu)

    def _print_exit_msg(self):
        print("See you later")

    def _get_numbers(self, ans):
        valid_num, invalid_num = [], []

        ans = ans.strip()
        numbers = ans.split(' ')

        for number in numbers:
            num = number.strip()
            if not is_number(num):
                invalid_num.append(num)
            else:
                valid_num.append(num)

        return valid_num, invalid_num

    def _get_op_idx(self, prompt):
        while True:
            ans = input(prompt).strip()
            valid, invalid = self._get_numbers(ans)

            if len(valid) == 0 and len(invalid) == 0:
                print("No input")
            elif len(valid) == 0:
                print("Invalid input")
            else:
                return valid[0]

    def _get_args(self, prompt):
        while True:
            ans = input(prompt).strip()
            valid, invalid = self._get_numbers(ans)

            if len(valid) == 0 and len(invalid) == 0:
                print("No input")
            elif len(valid) > 0:
                if len(invalid) > 0:
                    print(f"Warning: {invalid} are invalid and ignored")
                return self._parse_args(valid)

    def _parse_args(self, numbers):
        result = []

        for number in numbers:
            if is_integer(number):
                result.append(int(number))
            else:
                result.append(float(number))
        return result

    def _get_and_exec_input(self):
        op_idx = self._get_op_idx("Enter operation no. (-1 to exit): ")
        if op_idx == '-1':
            return None

        args = self._get_args("Enter arguments (separated by space): ")

        op_lbl = self.menu.get_op_lbl_from_idx(int(op_idx)-1)
        return self.controller.execute(op_lbl, args)
