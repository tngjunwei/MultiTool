from decimal import DivisionByZero
import unittest
from src.calculator.operators.arithmetic_operator import *

class TestAdd(unittest.TestCase):

    def test_add_integer(self):
        add = Add(args=[10, 5])
        self.assertEqual(add(), 15)

        add = Add(args=[-5, 10])
        self.assertEqual(add(), 5)

    def test_add_float(self):
        add = Add(args=[1.05, 0.15])
        self.assertAlmostEqual(add(), 1.2)

        add = Add(args=[1.05, -0.05])
        self.assertAlmostEqual(add(), 1.0)

class TestSubtract(unittest.TestCase):

    def test_subtract_integer(self):
        subtract = Subtract(args=[10, 5])
        self.assertEqual(subtract(), 5)

        subtract = Subtract(args=[-10, -5])
        self.assertEqual(subtract(), -5)
    
    def test_subtract_float(self):
        subtract = Subtract(args=[1.2, 0.2])
        self.assertAlmostEqual(subtract(), 1.0)

        subtract = Subtract(args=[-1.2, -0.2])
        self.assertAlmostEqual(subtract(), -1.0)

class TestMultiply(unittest.TestCase):

    def test_multiply_integer(self):
        multiply = Multiply(args=[2, 5])
        self.assertEqual(multiply(), 10)
    
        multiply = Multiply(args=[-2, -5])
        self.assertEqual(multiply(), 10)

        multiply = Multiply(args=[2, 0])
        self.assertEqual(multiply(), 0)

    def test_multiply_float(self):
        multiply = Multiply(args=[2.5, 5.5])
        self.assertEqual(multiply(), 13.75)


class TestDivision(unittest.TestCase):

    def test_divide_integer(self):
        divide = Divide(args=[8, 4])
        self.assertEqual(divide(), 2)

        divide = Divide(args=[8, 0])
        self.assertAlmostEqual(divide(), float("inf"))

        divide = Divide(args=[-8, 0])
        self.assertAlmostEqual(divide(), float("-inf"))
    
    def test_divide_float(self):
        divide = Divide(args=[10.0, 2.5])
        self.assertAlmostEqual(divide(), 4.0)

        divide = Divide(args=[8.0, 0.0])
        self.assertAlmostEqual(divide(), float("inf"))

        divide = Divide(args=[-8.0, 0.0])
        self.assertAlmostEqual(divide(), float("-inf"))
        