import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        # simple addition
        self.assertEqual(add(3, 4), 7)
        # negative number
        self.assertEqual(add(-5, 2), -3)
        # decimal addition
        self.assertAlmostEqual(add(1.5, 2.3), 3.8)

    def test_subtract(self): # 3 assertions
        # basic subtraction
        self.assertEqual(sub(10, 3), 7)
        # negative result
        self.assertEqual(sub(2, 5), -3)
        # decimals
        self.assertAlmostEqual(sub(5.5, 2.2), 3.3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-2, 3), -6)
        self.assertAlmostEqual(mul(2.2, 3), 6.6)
        self.assertAlmostEqual(mul(0, 3), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 2), 2)
        self.assertAlmostEqual(div(-2, 4), -2)
        self.assertAlmostEqual(div(2, 5), 2.5)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        # log base 10
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(math.e, math.e), 1)
        # log with decimal base
        self.assertAlmostEqual(log(2, 8), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    ## call log function inside, example:
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 5), 5)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.sqrt(1.5 ** 2 + 2.0 ** 2))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()