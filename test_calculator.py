import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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