'''
Unit tests for calculator functions
'''

import unittest
from calc import *

class TestCalc(unittest. TestCase):

    def test_add(self):
        self.assertEqual(calculate(['7', '+', '3']), 10)

        with self.assertRaises(CalcError):
            calculate('not a list')
    '''
    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    # create a divide test function

    def test_divide(self):
        pass

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
    '''

# Run the code within the conditional

if __name__ == '__main__':
    unittest.main()  