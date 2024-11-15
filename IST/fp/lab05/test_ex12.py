#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
SKIP = False
try :
    import ex12
except ImportError:
    SKIP = True
class TestEx12(unittest.TestCase):
    ''' test class for ex12.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex12.py")
        self.unit = ex12
    def test_1(self):
        ''' Test sequence for 'ANA' '''
        self.assertTrue(self.unit.palindromo("ANA"))
    def test_2(self):
        ''' Test sequence for 'ANAA' '''
        self.assertFalse(self.unit.palindromo("ANAA"))
    def test_3(self):
        ''' Test sequence for 'ANNA' '''
        self.assertTrue(self.unit.palindromo("ANNA"))
    def test_4(self):
        ''' Test sequence for 'ANANA' '''
        self.assertTrue(self.unit.palindromo("ANANA"))
    def test_5(self):
        ''' Test sequence for 'BANANA' '''
        self.assertFalse(self.unit.palindromo("BANANA"))
    def test_6(self):
        ''' Test sequence for 'BANANAB' '''
        self.assertTrue(self.unit.palindromo("BANANAB"))
    def test_7(self):
        ''' Test sequence for 'palindromo' '''
        self.assertFalse(self.unit.palindromo("palindromo"))
    def test_8(self):
        ''' Test sequence for '' '''
        self.assertFalse(self.unit.palindromo(""))
if __name__ == '__main__':
    unittest.main()
