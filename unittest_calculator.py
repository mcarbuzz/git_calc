import unittest
from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
from modulo import modulo
from power import power
from sine import sine
from cosine import cosine
from square_root import square_root
from floor_value import floor_value
from ceil_value import ceil_value
from memory_add import memory_add
from memory_clear import memory_clear
from memory import memory

class TestCalculator(unittest.TestCase):
    def setUp(self):
        memory_clear()  # Ensure memory starts at 0 for each test

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-2, 3), 1)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)
        self.assertEqual(multiplication(-4, 3), -12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(10, 3), 10 / 3)
        self.assertEqual(division(10, 0), "Error: Division by zero")

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 5), 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(90), 1)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(90), 0, places=5)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-4), "Error: Negative input")

    def test_floor_value(self):
        self.assertEqual(floor_value(3.7), 3)
        self.assertEqual(floor_value(-3.7), -4)

    def test_ceil_value(self):
        self.assertEqual(ceil_value(3.7), 4)
        self.assertEqual(ceil_value(-3.7), -3)


if __name__ == "__main__":
    unittest.main()
#python -m unittest unittest_calculator.py