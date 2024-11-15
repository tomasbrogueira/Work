#! /usr/bin/env python3
''' tests for ex09.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx09(unittest.TestCase):
    ''' test class for ex09.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex09.ebnf'):
            self.skipTest("no ex09.ebnf")
        if not self._gram:
            with open('ex09.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_xyz(self):
        ''' Test sequence for '(xyz)' '''
        self.assertTrue(parse('(xyz)'))
    def test_xyzxyzxyz(self):
        ''' Test sequence for '(xyzxyzxyz)' '''
        self.assertTrue(parse('(xyzxyzxyz)'))
    def test_empty(self):
        ''' Test sequence for '()' '''
        self.assertFalse(parse('()'))
    def test_xyzxyz(self):
        ''' Test sequence for '(xyzxyz)' '''
        self.assertFalse(parse('(xyzxyz)'))
if __name__ == '__main__':
    unittest.main()
