#! /usr/bin/env python3
''' tests for ex08.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx08(unittest.TestCase):
    ''' test class for ex08.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex08.ebnf'):
            self.skipTest("no ex08.ebnf")
        if not self._gram:
            with open('ex08.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for 'A1' '''
        self.assertTrue(parse('A1'))
    def test_2(self):
        ''' Test sequence for 'ABAAAAC333311' '''
        self.assertTrue(parse('ABAAAAC333311'))
    def test_3(self):
        ''' Test sequence for 'A' '''
        self.assertFalse(parse('A'))
    def test_4(self):
        ''' Test sequence for '1A1' '''
        self.assertFalse(parse('1A1'))
    def test_5(self):
        ''' Test sequence for '12AB' '''
        self.assertFalse(parse('12AB'))
    def test_6(self):
        ''' Test sequence for 'B2B' '''
        self.assertFalse(parse('B2B'))
if __name__ == '__main__':
    unittest.main()
