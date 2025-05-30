'''
Unit tests for calculator functions
'''

import unittest
from calc import *

class TestCalc(unittest. TestCase):

    def test_add(self):
        # Test 2 ints
        self.assertEqual(calculate(['7', '+', '3']), 10)

        # Test 2 floats
        self.assertEqual(calculate(['0.4', '+', '9.4']), 9.8)

        # Test float int
        self.assertEqual(calculate(['0.4', '+', '5']), 5.4)

        # Test int float 
        self.assertEqual(calculate(['5', '+', '5.4']), 10.4)

        # Test negative positive
        self.assertEqual(calculate(['-5', '+', '5.4']), 0.4)

        # Test positive negative
        self.assertEqual(calculate(['5', '+', '-5.4']), -0.4)

        # Test float float int result
        self.assertEqual(calculate(['5.5', '+', '-6.5']), -1)



        # bad operator
        with self.assertRaises(CalcError):
             calculate(['7', 'plus', '3'])

        # bad operands
        with self.assertRaises(ValueError):
            calculate(['d', '+', 'a'])

        with self.assertRaises(CalcError):
            calculate('not a list')


    def test_subtract(self):
        # Test 2 ints
        self.assertEqual(calculate(['7', '-', '3']), 4)

        # Test 2 floats
        self.assertEqual(calculate(['0.4', '-', '9.4']), 9)

        self.assertEqual(calculate(['0.4', '-', '5']), -4.6)

        self.assertEqual(calculate(['5', '-', '5.4']), 0.4)

        # bad operator
        with self.assertRaises(CalcError):
             calculate(['7', 'subtraction', '3'])

        # bad operands
        with self.assertRaises(ValueError):
            calculate(['d', '-', 'a'])

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