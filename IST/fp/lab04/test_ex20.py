#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
from math import atan
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
    def test_1(self):
        ''' Test sequence for '0 20' '''
        self.assertAlmostEqual(self.unit.arctan(0, 20), 0)
    def test_2(self):
        ''' Test sequence for '0.5 50' '''
        self.assertAlmostEqual(self.unit.arctan(.5, 50), atan(1), delta=.4)
    def test_3(self):
        ''' Test sequence for '1 20' '''
        self.assertAlmostEqual(self.unit.arctan(1, 20), atan(1), 6)
    def test_4(self):
        ''' Test sequence for '10 200' '''
        self.assertAlmostEqual(self.unit.arctan(10, 200), atan(100), delta=.2)
if __name__ == '__main__':
    unittest.main()
