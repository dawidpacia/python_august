import unittest
from hamcrest import *
from python_basics.python_functions import calculate_fuel

class FuelTests(unittest.TestCase):

    def test_12(self):
        assert_that(calculate_fuel(12), equal_to(2))

    def test_100756(self):
        assert_that(calculate_fuel(100756), equal_to(33583))

    def test_negative(self):
        assert_that(calculate_fuel(-1), equal_to(False))

    def test_zero(self):
        assert_that(calculate_fuel(0), equal_to(False))

    def test_1(self):
        assert_that(calculate_fuel(1), equal_to(1))

    def test_text(self):
        assert_that(calculate_fuel("ęśąćż"), equal_to(False))

if __name__ == "__main__":
    unittest.main()
