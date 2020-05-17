# -*- coding: utf-8 -*-
"""
@author: DUDO3
"""

import unittest

from Calc_class import Calculator

class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.Calculator = Calculator()

    def test_add(self):
        result = Calculator().add([2, 4], [2, 5])
        self.assertEqual([4, 9], result)
        result = Calculator().add([2, 2, 2], [-2, -4, -2])
        self.assertEqual([0, -2, 0], result)

    def test_sub(self):
        result = Calculator().sub([2, 4], [2, 5])
        self.assertEqual([0, -1], result)
        result = Calculator().sub([2, 2, 2], [-2, -4, -2])
        self.assertEqual([4, 6, 4], result)

    def test_multi(self):
        result = Calculator().multi([2, 4], [2, 5])
        self.assertEqual([4, 20], result)
        result = Calculator().multi([2, 2, 2], [-2, -4, -2])
        self.assertEqual([-4, -8, -4], result)

    def test_div(self):
        result = Calculator().div([2, 15], [2, 5])
        self.assertEqual([1, 3], result)
        result = Calculator().div([2, 2, 2], [2, 0, 2])
        self.assertEqual('N/A', result)

    def test_square_root(self):
        result = Calculator().square_root([16, 25])
        self.assertEqual([4, 5], result)
        result = Calculator().square_root([0, 225, 25])
        self.assertEqual([0, 15, 5], result)

    def test_square(self):
        result = Calculator().square([2, 4])
        self.assertEqual([4, 16], result)
        result = Calculator().square([8, -2, 2])
        self.assertEqual([64, 4, 4], result)

    def test_power(self):
        result = Calculator().power([2, 3, 4], [2, 2, 2])
        self.assertEqual([4, 9, 16], result)

    def test_sumlist(self):
        result = Calculator().sumlist([2, 5, 7])
        self.assertEqual(14, result)
        result = Calculator().sumlist([2, -2, 7, -15, 3, 7])
        self.assertEqual(2, result)

    def test_conv_lbs_to_kg(self):
        result = Calculator().conv_lbs_to_kg([1, 10, 20])
        self.assertEqual([0.45, 4.54, 9.07], result)

    def test_conv_C_to_F(self):
        result = Calculator().conv_C_to_F([0, 37.5, 100])
        self.assertEqual([32, 99.5, 212], result)

        
    def test_odd(self):
        result = Calculator().odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual([1, 3, 5, 7, 9], result)

    def test_even(self):
        result = Calculator().even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual([2, 4, 6, 8, 10], result)
        
if __name__ == '__main__':
    unittest.main()