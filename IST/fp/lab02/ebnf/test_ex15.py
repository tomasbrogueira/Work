#! /usr/bin/env python3
''' tests for ex15.ebnf '''
from os.path import exists
import unittest
from ebnf import grammar, parse
class TestEx15(unittest.TestCase):
    ''' test class for ex15.ebnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load ebnf grammar '''
        if not exists('ex15.ebnf'):
            self.skipTest("no ex15.ebnf")
        if not self._gram:
            with open('ex15.ebnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for 'AH-51-83' '''
        self.assertTrue(parse('AH-51-83'))
    def test_2(self):
        ''' Test sequence for '15-42-DA' '''
        self.assertTrue(parse('15-42-DA'))
    def test_3(self):
        ''' Test sequence for '74-FZ-72' '''
        self.assertTrue(parse('74-FZ-72'))
    def test_4(self):
        ''' Test sequence for 'AC-38-PO' '''
        self.assertTrue(parse('AC-38-PO'))
    def test_5(self):
        ''' Test sequence for 'AC-FZ-PO' '''
        self.assertFalse(parse('AC-FZ-PO'))
    def test_6(self):
        ''' Test sequence for 'A1-B2-C3' '''
        self.assertFalse(parse('A1-B2-C3'))
    def test_7(self):
        ''' Test sequence for '12-34-56' '''
        self.assertFalse(parse('12-34-56'))
    def test_8(self):
        ''' Test sequence for '12-AF-ZE' '''
        self.assertFalse(parse('12-AF-ZE'))
    def test_9(self):
        ''' Test sequence for 'UI-JH-37' '''
        self.assertFalse(parse('UI-JH-37'))
    def test_10(self):
        ''' Test sequence for 'po-12-44' '''
        self.assertFalse(parse('po-12-44'))
if __name__ == '__main__':
    unittest.main()
