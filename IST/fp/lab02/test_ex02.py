#! /usr/bin/env python3
''' tests for ex02.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx02(unittest.TestCase):
    ''' test class for ex02.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex02.bnf'):
            self.skipTest("no ex02.bnf")
        if not self._gram:
            with open('ex02.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test the 'ABCD' sequence '''
        self.assertFalse(parse('ABCD'))
    def test_2(self):
        ''' Test the '1CD' sequence '''
        self.assertFalse(parse('1CD'))
    def test_3(self):
        ''' Test the 'A123CD' sequence '''
        self.assertFalse(parse('A123CD'))
    def test_4(self):
        ''' Test the 'AAAAB12' sequence '''
        self.assertTrue(parse('AAAAB12'))
    def test_5(self):
        ''' Test the 'A1' sequence '''
        self.assertTrue(parse('A1'))
    def test_6(self):
        ''' Test the 'A4321' sequence '''
        self.assertTrue(parse('A4321'))
    def test_7(self):
        ''' Test the 'ABCD' sequence '''
        self.assertFalse(parse('4444'))
if __name__ == '__main__':
    unittest.main()
