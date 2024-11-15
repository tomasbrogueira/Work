#! /usr/bin/env python3
''' tests for ex19.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx19(unittest.TestCase):
    ''' test class for ex19.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex19.bnf'):
            self.skipTest("no ex19.bnf")
        if not self._gram:
            with open('ex19.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for '[0x1a2b : 0xfffff : 0x0000]' '''
        self.assertTrue(parse('[0x1a2b : 0xfffff : 0x0000]'))
    def test_2(self):
        ''' Test sequence for '[0x1 : 0xF : 0x0]' '''
        self.assertTrue(parse('[0x1 : 0xF : 0x0]'))
    def test_3(self):
        ''' Test sequence for '[0x1a2b]' '''
        self.assertTrue(parse('[0x1a2b]'))
    def test_4(self):
        ''' Test sequence for '[]' '''
        self.assertFalse(parse('[]'))
    def test_5(self):
        ''' Test sequence for '[ : ]' '''
        self.assertFalse(parse('[ : ]'))
    def test_6(self):
        ''' Test sequence for '[0x1a2b 0xfffff 0x0000]' '''
        self.assertFalse(parse('[0x1a2b 0xfffff 0x0000]'))
    def test_7(self):
        ''' Test sequence for '[0xFADA : 0xface : 0xBeBe]' '''
        self.assertTrue(parse('[0xFADA : 0xface : 0xBeBe]'))
if __name__ == '__main__':
    unittest.main()
