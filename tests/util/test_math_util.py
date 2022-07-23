import unittest
from src.util.math_util import *

class TestNumericString(unittest.TestCase):

    def test_is_integer(self):
        self.assertTrue(is_integer('5'))
        self.assertTrue(is_integer('-5'))
        
        self.assertFalse(is_integer('5.0'))
        self.assertFalse(is_integer('a'))
        self.assertFalse(is_integer(''))
    
    def test_is_float(self):
        self.assertTrue(is_float('5.0'))
        self.assertTrue(is_float('-5.0'))
        self.assertTrue(is_float('5.'))

        self.assertFalse(is_float('a'))
        self.assertFalse(is_float('5'))