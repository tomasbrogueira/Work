#! /usr/bin/env python3
''' tests for ex04.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx04(unittest.TestCase):
    ''' test class for ex04.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex04.ebnf'):
            self.skipTest("no ex04.ebnf")
        if not self._gram:
            with open('ex04.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_0(self):
        ''' Test for the '0' sequence '''
        self.assertTrue(parse('0'))
    def test_1(self):
        ''' Test for the '1' sequence '''
        self.assertTrue(parse('1'))
    def test_12349(self):
        ''' Test for the '12349' sequence '''
        self.assertTrue(parse('12349'))
    def test_012(self):
        ''' Test for the '012' sequence '''
        self.assertFalse(parse('012'))
    def test_00(self):
        ''' Test for the '00' sequence '''
        self.assertFalse(parse('00'))
if __name__ == '__main__':
    unittest.main()
