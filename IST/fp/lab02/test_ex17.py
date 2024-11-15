#! /usr/bin/env python3
''' tests for ex17.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx17(unittest.TestCase):
    ''' test class for ex17.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex17.bnf'):
            self.skipTest("no ex17.bnf")
        if not self._gram:
            with open('ex17.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for 'abcdbcde' '''
        self.assertTrue(parse('abcdbcde'))
    def test_2(self):
        ''' Test sequence for 'abcdbcdbcdbcde' '''
        self.assertTrue(parse('abcdbcdbcdbcde'))
    def test_3(self):
        ''' Test sequence for 'abcde' '''
        self.assertFalse(parse('abcde'))
    def test_4(self):
        ''' Test sequence for 'abcdbcdbcde' '''
        self.assertFalse(parse('abcdbcdbcde'))
    def test_5(self):
        ''' Test sequence for 'ae' '''
        self.assertFalse(parse('ae'))
    def test_6(self):
        ''' Test sequence for 'abcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcde' '''
        self.assertTrue(parse('abcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcde'))
    def test_7(self):
        ''' Test sequence for 'abc...cde' '''
        self.assertTrue(parse('abcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdb'
            'cdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcdbcde'))
if __name__ == '__main__':
    unittest.main()
