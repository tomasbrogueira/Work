#! /usr/bin/env python3
''' tests for ex13.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx13(unittest.TestCase):
    ''' test class for ex13.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex13.bnf'):
            self.skipTest("no ex13.bnf")
        if not self._gram:
            with open('ex13.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '{a:1,b:2,c:3}' '''
        self.assertTrue(parse('{a:1,b:2,c:3}'))
    def test_2(self):
        ''' Test sequence for '{a:1}' '''
        self.assertTrue(parse('{a:1}'))
    def test_3(self):
        ''' Test sequence for '{a:0,b:00,c:000}' '''
        self.assertTrue(parse('{a:0,b:00,c:000}'))
    def test_4(self):
        ''' Test sequence for '{a:1,aa:2,aaa:3}' '''
        self.assertTrue(parse('{a:1,aa:2,aaa:3}'))
    def test_5(self):
        ''' Test sequence for '{a:1,b:2,}' '''
        self.assertFalse(parse('{a:1,b:2,}'))
    def test_6(self):
        ''' Test sequence for '{a:1,b:,c:3}' '''
        self.assertFalse(parse('{a:1,b:,c:3}'))
    def test_7(self):
        ''' Test sequence for '{a:1,2:b,c:3}' '''
        self.assertFalse(parse('{a:1,2:b,c:3}'))
    def test_8(self):
        ''' Test sequence for '{}' '''
        self.assertFalse(parse('{}'))
if __name__ == '__main__':
    unittest.main()
