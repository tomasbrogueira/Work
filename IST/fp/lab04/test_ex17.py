#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
from math import sin, sqrt, pi
SKIP = False
try :
    import ex17
except ImportError:
    SKIP = True
class TestEx17(unittest.TestCase):
    ''' test class for ex17.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex17.py")
        self.unit = ex17
    def test_1(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.seno(0, 20), 0)
    def test_2(self):
        ''' Test sequence for 'pi/2' '''
        self.assertAlmostEqual(self.unit.seno(pi/2, 20), 1)
    def test_3(self):
        ''' Test sequence for 'pi/4' '''
        self.assertAlmostEqual(self.unit.seno(pi/4, 20), sqrt(2)/2)
    def test_4(self):
        ''' Test sequence for '2' '''
        self.assertAlmostEqual(self.unit.seno(2, 20), sin(2))
if __name__ == '__main__':
    unittest.main()
