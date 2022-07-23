'''This module contains the OperatorMenu class.'''


class OperatorMenu:
    '''The OperatorMenu class provides a mapping between user input and
     the operator to execute.'''

    def __init__(self, operator_map):
        self.operator_map = operator_map
        self.list_op_lbl = list(self.operator_map.keys())
        self.list_op_desc = [op.desc() for op in operator_map.values()]

    def __str__(self):
        menu = ''

        counter = range(1, len(self.operator_map)+1)
        for entry in zip(counter, self.list_op_lbl, self.list_op_desc):
            menu += f"{entry[0]}: {entry[1]} - {entry[2]}\n"
        return menu

    def get_op_lbl_from_idx(self, idx):
        '''Returns the operator label.'''
        return self.list_op_lbl[idx]
