#! /usr/bin/env python3
''' tests for ex16.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx16(unittest.TestCase):
    ''' test class for ex16.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex16.bnf'):
            self.skipTest("no ex16.bnf")
        if not self._gram:
            with open('ex16.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '20h23m45s' '''
        self.assertTrue(parse('20h23m45s'))
    def test_2(self):
        ''' Test sequence for '23h59m59s' '''
        self.assertTrue(parse('23h59m59s'))
    def test_3(self):
        ''' Test sequence for '00h00m00s' '''
        self.assertTrue(parse('00h00m00s'))
    def test_4(self):
        ''' Test sequence for '20h60m45s' '''
        self.assertFalse(parse('20h60m45s'))
    def test_5(self):
        ''' Test sequence for '20h23m60s' '''
        self.assertFalse(parse('20h23m60s'))
    def test_6(self):
        ''' Test sequence for '24h23m45s' '''
        self.assertFalse(parse('24h23m45s'))
    def test_7(self):
        ''' Test sequence for '20h23m' '''
        self.assertFalse(parse('20h23m'))
    def test_8(self):
        ''' Test sequence for '20h' '''
        self.assertFalse(parse('20h'))
    def test_9(self):
        ''' Test sequence for '8h23m45s' '''
        self.assertFalse(parse('8h23m45s'))
    def test_10(self):
        ''' Test sequence for '20h3m45s' '''
        self.assertFalse(parse('20h3m45s'))
if __name__ == '__main__':
    unittest.main()
