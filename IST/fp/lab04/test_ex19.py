#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
from math import asin, sqrt, pi
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        self.unit = ex19
    def test_1(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.arco_seno(0, 20), 0)
    def test_2(self):
        ''' Test sequence for '1' '''
        self.assertAlmostEqual(self.unit.arco_seno(1, 50), pi/2, delta=.1)
    def test_3(self):
        ''' Test sequence for 'sqrt(2)/2' '''
        self.assertAlmostEqual(self.unit.arco_seno(sqrt(2)/2, 20), pi/4)
    def test_4(self):
        ''' Test sequence for '0.5' '''
        self.assertAlmostEqual(self.unit.arco_seno(.5, 20), asin(.5))
if __name__ == '__main__':
    unittest.main()
