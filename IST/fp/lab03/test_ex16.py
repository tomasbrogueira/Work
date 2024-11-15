#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
SKIP = False
try :
    import ex16
except ImportError:
    SKIP = True
class TestEx16(unittest.TestCase):
    ''' test class for ex16.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex16.py")
        self.unit = ex16
    def test_2017(self):
        ''' Test sequence with number 2017 '''
        self.assertFalse(self.unit.bissexto(2017))
    def test_2016(self):
        ''' Test sequence with number 2016 '''
        self.assertTrue(self.unit.bissexto(2016))
    def test_2000(self):
        ''' Test sequence with number 2000 '''
        self.assertTrue(self.unit.bissexto(2000))
    def test_1900(self):
        ''' Test sequence with number 1900 '''
        self.assertFalse(self.unit.bissexto(1900))
    def test_2020(self):
        ''' Test sequence with number 2020 '''
        self.assertTrue(self.unit.bissexto(2020))
    def test_2022(self):
        ''' Test sequence with number 2022 '''
        self.assertFalse(self.unit.bissexto(2022))
    def test_2024(self):
        ''' Test sequence with number 2024 '''
        self.assertTrue(self.unit.bissexto(2024))
    def test_1100(self):
        ''' Test sequence with number 1100 '''
        self.assertFalse(self.unit.bissexto(1100))
if __name__ == '__main__':
    unittest.main()
