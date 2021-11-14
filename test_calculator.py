import unittest
from calculator import is_even


class TestCalculator(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual('it is odd', is_even(5))

