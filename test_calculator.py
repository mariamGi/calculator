import unittest
from calculator import is_even, calculator


class TestCalculator(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual('it is odd', is_even(5))

    def test_calculation(self):
        self.assertEqual(250.25, calculator(350))
