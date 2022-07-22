from decimal import DivisionByZero
import unittest
from src.calculator.operators.arithmetic_operator import *

class TestAdd(unittest.TestCase):

    def test_add_integer(self):
        add = Add(first=5, second=10)
        self.assertEqual(add(), 15)

        add = Add(first=-5, second=10)
        self.assertEqual(add(), 5)

    def test_add_float(self):
        add = Add(first=1.05, second=0.15)
        self.assertAlmostEqual(add(), 1.2)

        add = Add(first=1.05, second=-0.05)
        self.assertAlmostEqual(add(), 1.0)

class TestSubtract(unittest.TestCase):

    def test_subtract_integer(self):
        subtract = Subtract(first=10, second=5)
        self.assertEqual(subtract(), 5)

        subtract = Subtract(first=-10, second=-5)
        self.assertEqual(subtract(), -5)
    
    def test_subtract_float(self):
        subtract = Subtract(first=1.2, second=0.2)
        self.assertAlmostEqual(subtract(), 1.0)

        subtract = Subtract(first=-1.2, second=-0.2)
        self.assertAlmostEqual(subtract(), -1.0)

class TestMultiply(unittest.TestCase):

    def test_multiply_integer(self):
        multiply = Multiply(first=2, second=5)
        self.assertEqual(multiply(), 10)
    
        multiply = Multiply(first=-2, second=-5)
        self.assertEqual(multiply(), 10)

        multiply = Multiply(first=2, second=0)
        self.assertEqual(multiply(), 0)

    def test_multiply_float(self):
        multiply = Multiply(first=2.5, second=5.5)
        self.assertEqual(multiply(), 13.75)


class TestDivision(unittest.TestCase):

    def test_divide_integer(self):
        divide = Divide(first=8, second=4)
        self.assertEqual(divide(), 2)

        with self.assertRaises(ZeroDivisionError):
            divide = Divide(first=8, second=0)
            divide()
    
    def test_divide_float(self):
        divide = Divide(first=10.0, second=2.5)
        self.assertAlmostEqual(divide(), 4.0)

        with self.assertRaises(ZeroDivisionError):
            divide = Divide(first=8.0, second=0.0)
            divide()
        