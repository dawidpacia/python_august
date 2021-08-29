import unittest

from hamcrest import *

from python_basics.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_add(self):
        assert_that(self.calculator.add_values(1, 2), equal_to(3))

    def test_div(self):
        assert_that(self.calculator.div_values(1, 2), equal_to(0.5))

    def test_zero_division(self):
        assert_that(self.calculator.div_values(1, 0), equal_to(False))
