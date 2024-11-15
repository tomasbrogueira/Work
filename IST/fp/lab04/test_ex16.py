#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
from math import exp, e
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
    def test_0(self):
        ''' Test sequence for '1.2' '''
        self.assertAlmostEqual(self.unit.expon(1.2, 20), exp(1.2))
    def test_1(self):
        ''' Test sequence for '0.8' '''
        self.assertAlmostEqual(self.unit.expon(.8, 20), exp(.8))
    def test_2(self):
        ''' Test sequence for '-0.8' '''
        self.assertAlmostEqual(self.unit.expon(-.8, 20), exp(-.8))
    def test_3(self):
        ''' Test sequence for '1' '''
        self.assertAlmostEqual(self.unit.expon(1, 20), e)
    def test_4(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.expon(0, 20), 1.)
if __name__ == '__main__':
    unittest.main()
