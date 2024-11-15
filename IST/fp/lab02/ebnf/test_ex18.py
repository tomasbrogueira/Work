#! /usr/bin/env python3
''' tests for ex18.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx18(unittest.TestCase):
    ''' test class for ex18.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex18.ebnf'):
            self.skipTest("no ex18.ebnf")
        if not self._gram:
            with open('ex18.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '1.0+0.0i' '''
        self.assertTrue(parse('1.0+0.0i'))
    def test_2(self):
        ''' Test sequence for '1.0+-0.0i' '''
        self.assertFalse(parse('1.0+-0.0i'))
    def test_3(self):
        ''' Test sequence for '-1.0+0.0i' '''
        self.assertTrue(parse('-1.0+0.0i'))
    def test_4(self):
        ''' Test sequence for '0.0+0.0i' '''
        self.assertTrue(parse('0.0+0.0i'))
    def test_5(self):
        ''' Test sequence for '-1.0-0.0i' '''
        self.assertTrue(parse('-1.0-0.0i'))
    def test_6(self):
        ''' Test sequence for '1.0++0.0i' '''
        self.assertFalse(parse('1.0++0.0i'))
    def test_7(self):
        ''' Test sequence for '-i' '''
        self.assertFalse(parse('-i'))
    def test_8(self):
        ''' Test sequence for '+i' '''
        self.assertFalse(parse('+i'))
    def test_9(self):
        ''' Test sequence for '1+0i' '''
        self.assertFalse(parse('1+0i'))
    def test_10(self):
        ''' Test sequence for '1.0-0.0i' '''
        self.assertTrue(parse('1.0-0.0i'))
if __name__ == '__main__':
    unittest.main()
