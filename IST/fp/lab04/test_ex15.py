#! /usr/bin/env python3
''' tests for ex15.py '''
import unittest
from math import log
SKIP = False
try :
    import ex15
except ImportError:
    SKIP = True
class TestEx15(unittest.TestCase):
    ''' test class for ex15.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex15.py")
        self.unit = ex15
    def test_0(self):
        ''' Test sequence for '5' '''
        self.assertAlmostEqual(self.unit.logn(5, 20), log(5))
    def test_1(self):
        ''' Test sequence for '3' '''
        self.assertAlmostEqual(self.unit.logn(3, 20), log(3))
    def test_2(self):
        ''' Test sequence for '2.1' '''
        self.assertAlmostEqual(self.unit.logn(2.1, 10), log(2.1))
    def test_3(self):
        ''' Test sequence for '1.1' '''
        self.assertAlmostEqual(self.unit.logn(1.1, 10), log(1.1))
    def test_4(self):
        ''' Test sequence for '1.2' '''
        self.assertAlmostEqual(self.unit.logn(1.2, 10), log(1.2))
    def test_5(self):
        ''' Test sequence for '1.3' '''
        self.assertAlmostEqual(self.unit.logn(1.3, 10), log(1.3))
    def test_6(self):
        ''' Test sequence for '1.4' '''
        self.assertAlmostEqual(self.unit.logn(1.4, 10), log(1.4))
if __name__ == '__main__':
    unittest.main()
