#! /usr/bin/env python3
''' tests for ex10.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx10(unittest.TestCase):
    ''' test class for ex10.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex10.bnf'):
            self.skipTest("no ex10.bnf")
        if not self._gram:
            with open('ex10.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_13(self):
        ''' Test sequence for '1.3E-45' '''
        self.assertTrue(parse('1.3E-45'))
    def test_013(self):
        ''' Test sequence for '01.3E-45' '''
        self.assertFalse(parse('01.3E-45'))
    def test_1003(self):
        ''' Test sequence for '1.003E-45' '''
        self.assertTrue(parse('1.003E-45'))
    def test_1(self):
        ''' Test sequence for '1E-45' '''
        self.assertFalse(parse('1E-45'))
    def test_1_(self):
        ''' Test sequence for '1.E-45' '''
        self.assertFalse(parse('1.E-45'))
    def test_noexp(self):
        ''' Test sequence for '1.3' '''
        self.assertFalse(parse('1.3'))
    def test_plus(self):
        ''' Test sequence for '1.3E+45' '''
        self.assertTrue(parse('1.3E+45'))
    def test_omit(self):
        ''' Test sequence for '1.3E45' '''
        self.assertTrue(parse('1.3E45'))
if __name__ == '__main__':
    unittest.main()
