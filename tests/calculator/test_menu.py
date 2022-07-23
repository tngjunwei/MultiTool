import unittest
from src.calculator.menu import OperatorMenu

class TestOperatorMenu(unittest.TestCase):

    def test_empty_menu(self):
        menu = OperatorMenu({})
        self.assertEqual(str(menu), '')
