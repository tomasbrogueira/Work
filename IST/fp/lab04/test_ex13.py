#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
from math import sqrt
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
    def test_12(self):
        ''' Test sequence for '12' '''
        self.assertAlmostEqual(self.unit.sqroot(12), sqrt(12))
    def test_12_approx(self):
        ''' Test sequence for '12' with 'eps' '''
        self.assertNotAlmostEqual(self.unit.sqroot(12, eps=1e-6), sqrt(12), delta=1e-8)
    def test_0(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.sqroot(0), 0)
    def test_25(self):
        ''' Test sequence for '25' '''
        self.assertAlmostEqual(self.unit.sqroot(25), 5)
if __name__ == '__main__':
    unittest.main()
