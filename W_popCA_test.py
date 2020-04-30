# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:00:30 2020

@author: DUDO3
"""

import unittest

import W_popCA


class TestW_popCA(unittest.TestCase):

    def setUp(self):
        self.contents = W_popCA.get_page_contents()

    def test_get_page(self):
        self.assertTrue(len(self.contents) > 0)

    def test_convert_to_soup(self):
        self.assertTrue(W_popCA.convert_to_soup(self.contents) is not None)

    def test_get_table(self):
        soup = W_popCA.convert_to_soup(self.contents)
        self.assertTrue(W_popCA.get_table(soup) is not None)

    def test_get_headers(self):
        soup = W_popCA.convert_to_soup(self.contents)
        table = W_popCA.get_table(soup)
        self.assertTrue(len(W_popCA.get_headers(table)) == 12)
    
    def test_get_rows(self):
        soup = W_popCA.convert_to_soup(self.contents)
        table = W_popCA.get_table(soup)
        self.assertTrue(len(W_popCA.get_rows(table)) == 235)
    

if __name__ == '__main__':
    unittest.main()