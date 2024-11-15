#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
from math import cos, sqrt, pi
SKIP = False
try :
    import ex18
except ImportError:
    SKIP = True
class TestEx18(unittest.TestCase):
    ''' test class for ex18.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex18.py")
        self.unit = ex18
    def test_1(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.coseno(0, 20), 1)
    def test_2(self):
        ''' Test sequence for 'pi/2' '''
        self.assertAlmostEqual(self.unit.coseno(pi/2, 20), 0)
    def test_3(self):
        ''' Test sequence for 'pi/4' '''
        self.assertAlmostEqual(self.unit.coseno(pi/4, 20), sqrt(2)/2)
    def test_4(self):
        ''' Test sequence for '2' '''
        self.assertAlmostEqual(self.unit.coseno(2, 20), cos(2))
if __name__ == '__main__':
    unittest.main()
