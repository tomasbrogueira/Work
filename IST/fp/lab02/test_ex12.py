#! /usr/bin/env python3
''' tests for ex12.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx12(unittest.TestCase):
    ''' test class for ex12.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex12.bnf'):
            self.skipTest("no ex12.bnf")
        if not self._gram:
            with open('ex12.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_1(self):
        ''' Test sequence for "+41.40338,-2.17403" '''
        self.assertTrue(parse("+41.40338,-2.17403"))
    def test_2(self):
        ''' Test sequence for "-41.4,-2.17" '''
        self.assertTrue(parse("-41.4,-2.17"))
    def test_3(self):
        ''' Test sequence for "+0.0,-0.0" '''
        self.assertTrue(parse("+0.0,-0.0"))
    def test_4(self):
        ''' Test sequence for "-1.00000,+2.00000" '''
        self.assertTrue(parse("-1.00000,+2.00000"))
    def test_5(self):
        ''' Test sequence for "41.40338,-2.17403" '''
        self.assertTrue(parse("41.40338,-2.17403"))
    def test_6(self):
        ''' Test sequence for "+0012.40,-2.10" '''
        self.assertFalse(parse("+0012.40,-2.10"))
    def test_7(self):
        ''' Test sequence for "+41.40338,-.17403" '''
        self.assertFalse(parse("+41.40338,-.17403"))
    def test_8(self):
        ''' Test sequence for "41,-9" '''
        self.assertFalse(parse("41,-9"))
    def test_9(self):
        ''' Test sequence for "0.0,0.0" '''
        self.assertTrue(parse("0.0,0.0"))
if __name__ == '__main__':
    unittest.main()
