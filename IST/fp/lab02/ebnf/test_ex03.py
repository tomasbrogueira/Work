#! /usr/bin/env python3
''' tests for ex03.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx03(unittest.TestCase):
    ''' test class for ex03.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex03.ebnf'):
            self.skipTest("no ex03.ebnf")
        if not self._gram:
            with open('ex03.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_abcba(self):
        ''' Test 'abcba' sequence '''
        self.assertTrue(parse('abcba'))
    def test_abcccba(self):
        ''' Test 'abcccba' sequence '''
        self.assertTrue(parse('abcccba'))
    def test_abba(self):
        ''' Test 'abba' sequence '''
        self.assertFalse(parse('abba'))
    def test_abca(self):
        ''' Test 'abca' sequence '''
        self.assertFalse(parse('abca'))
    def test_abccaccba(self):
        ''' Test 'abccaccba' sequence '''
        self.assertFalse(parse('abccaccba'))
if __name__ == '__main__':
    unittest.main()
