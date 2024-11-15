#! /usr/bin/env python3
''' tests for ex05.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx05(unittest.TestCase):
    ''' test class for ex05.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex05.bnf'):
            self.skipTest("no ex05.bnf")
        if not self._gram:
            with open('ex05.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_6284(self):
        ''' Test sequence for '(6-284)' sequence '''
        self.assertTrue(parse('(6-284)'))
    def test_8642(self):
        ''' Test sequence for '(864/2)' sequence '''
        self.assertTrue(parse('(864/2)'))
    def test_2486(self):
        ''' Test sequence for '(24*86)' sequence '''
        self.assertTrue(parse('(24*86)'))
    def test_82(self):
        ''' Test sequence for '(8+2)' sequence '''
        self.assertTrue(parse('(8+2)'))
    def test_12(self):
        ''' Test sequence for '(1+2)' sequence '''
        self.assertFalse(parse('(1+2)'))
    def test_2(self):
        ''' Test sequence for '(2+-)' sequence '''
        self.assertFalse(parse('(2+-)'))
    def test_2406(self):
        ''' Test sequence for '(24*06)' sequence '''
        self.assertTrue(parse('(24*06)'))
    def test_20(self):
        ''' Test sequence for '(2*0)' sequence '''
        self.assertFalse(parse('2*0'))
    def test_84(self):
        ''' Test sequence for '(8 4+)' sequence '''
        self.assertFalse(parse('(8 4+)'))
    def test_00(self):
        ''' Test sequence for '(0/0)' sequence '''
        self.assertTrue(parse('(0/0)'))
    def test_24(self):
        ''' Test sequence for '(2 + 4)' sequence '''
        self.assertFalse(parse('(2 + 4)'))
if __name__ == '__main__':
    unittest.main()
