#! /usr/bin/env python3
''' tests for ex14.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx14(unittest.TestCase):
    ''' test class for ex14.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex14.ebnf'):
            self.skipTest("no ex14.ebnf")
        if not self._gram:
            with open('ex14.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '(Joao,ANTONIO,PeDrO)' '''
        self.assertTrue(parse('(Joao,ANTONIO,PeDrO)'))
    def test_2(self):
        ''' Test sequence for '(Ana)' '''
        self.assertTrue(parse('(Ana)'))
    def test_3(self):
        ''' Test sequence for '()' '''
        self.assertFalse(parse('()'))
    def test_4(self):
        ''' Test sequence for '(,ana)' '''
        self.assertFalse(parse('(,ana)'))
    def test_5(self):
        ''' Test sequence for '(ana,)' '''
        self.assertFalse(parse('(ana,)'))
    def test_6(self):
        ''' Test sequence for '(ana)' '''
        self.assertFalse(parse('(ana)'))
if __name__ == '__main__':
    unittest.main()