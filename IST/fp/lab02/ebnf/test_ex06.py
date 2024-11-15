#! /usr/bin/env python3
''' tests for ex06.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx06(unittest.TestCase):
    ''' test class for ex06.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex06.ebnf'):
            self.skipTest("no ex06.ebnf")
        if not self._gram:
            with open('ex06.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_caaddaar(self):
        ''' Teste sequence for 'caaddaar' '''
        self.assertTrue(parse('caaddaar'))
    def test_cdr(self):
        ''' Teste sequence for 'cdr' '''
        self.assertTrue(parse('cdr'))
    def test_cd(self):
        ''' Teste sequence for 'cd' '''
        self.assertFalse(parse('cd'))
    def test_cdrr(self):
        ''' Teste sequence for 'cdrr' '''
        self.assertFalse(parse('cdrr'))
    def test_cadaar(self):
        ''' Teste sequence for 'cadaar' '''
        self.assertTrue(parse('cadaar'))
if __name__ == '__main__':
    unittest.main()
