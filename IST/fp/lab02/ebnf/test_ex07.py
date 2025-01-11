#! /usr/bin/env python3
''' tests for ex07.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx07(unittest.TestCase):
    ''' test class for ex07.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex07.ebnf'):
            self.skipTest("no ex07.ebnf")
        if not self._gram:
            with open('ex07.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_postal(self):
        ''' Test sequence for '1111-111' '''
        self.assertTrue(parse('1111-111'))
    def test_lead_zero(self):
        ''' Test sequence for '0111-111' '''
        self.assertFalse(parse('0111-111'))
    def test_short_code(self):
        ''' Test sequence for '111-111' '''
        self.assertFalse(parse('111-111'))
    def test_short_street(self):
        ''' Test sequence for '1111-11' '''
        self.assertFalse(parse('1111-11'))
    def test_long_street(self):
        ''' Test sequence for '1111-1111' '''
        self.assertFalse(parse('1111-1111'))
if __name__ == '__main__':
    unittest.main()