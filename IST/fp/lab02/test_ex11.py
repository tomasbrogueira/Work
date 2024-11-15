#! /usr/bin/env python3
''' tests for ex11.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx11(unittest.TestCase):
    ''' test class for ex11.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex11.bnf'):
            self.skipTest("no ex11.bnf")
        if not self._gram:
            with open('ex11.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for "41º24'12\"N,2º10'26\"W" '''
        self.assertTrue(parse("41º24'12\"N,2º10'26\"W"))
    def test_2(self):
        ''' Test sequence for "1º42'21\"S,112º01'52\"E" '''
        self.assertTrue(parse("1º42'21\"S,112º01'52\"E"))
    def test_3(self):
        ''' Test sequence for "41º4'12\"N,2º10'26\"W" '''
        self.assertFalse(parse("41º4'12\"N,2º10'26\"W"))
    def test_4(self):
        ''' Test sequence for "41º24'12\"E,2º10'26\"N" '''
        self.assertFalse(parse("41º24'12\"E,2º10'26\"N"))
    def test_5(self):
        ''' Test sequence for "41º24'N,2º10'26\"W" '''
        self.assertFalse(parse("41º24'N,2º10'26\"W"))
    def test_6(self):
        ''' Test sequence for "41º24'12\"N,2º10'26\"w" '''
        self.assertFalse(parse("41º24'12\"N,2º10'26\"w"))
    def test_7(self):
        ''' Test sequence for "1º42'21\"S,112º01'62\"E" '''
        self.assertFalse(parse("1º42'21\"S,112º01'62\"E"))
if __name__ == '__main__':
    unittest.main()
