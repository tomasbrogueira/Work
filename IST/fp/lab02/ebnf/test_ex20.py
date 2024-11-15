#! /usr/bin/env python3
''' tests for ex20.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx20(unittest.TestCase):
    ''' test class for ex20.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex20.ebnf'):
            self.skipTest("no ex20.ebnf")
        if not self._gram:
            with open('ex20.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '2021/11/02 Thu' '''
        self.assertTrue(parse('2021/11/02 Thu'))
    def test_2(self):
        ''' Test sequence for '2019/09/18 Mon' '''
        self.assertTrue(parse('2019/09/18 Mon'))
    def test_3(self):
        ''' Test sequence for '2021/11/02 Seg' '''
        self.assertFalse(parse('2021/11/02 Seg'))
    def test_4(self):
        ''' Test sequence for '2021/11/2 Thu' '''
        self.assertFalse(parse('2021/11/2 Thu'))
    def test_5(self):
        ''' Test sequence for '21/11/02 Thu' '''
        self.assertFalse(parse('21/11/02 Thu'))
    def test_6(self):
        ''' Test sequence for '2021/11/02 thu' '''
        self.assertFalse(parse('2021/11/02 thu'))
    def test_7(self):
        ''' Test sequence for '2021-11-02 Thu' '''
        self.assertFalse(parse('2021-11-02 Thu'))
if __name__ == '__main__':
    unittest.main()
