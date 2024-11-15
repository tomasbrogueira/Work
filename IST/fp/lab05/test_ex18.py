#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
from math import nan
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
        self.pos = (0, .1, .25, .5, .8, 1.)
        self.val = (1., 1.0101, 1.0645, 1.284, 1.8965, 2.7183)
    def test_1(self):
        ''' Test sequence for '.6' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, .6), 1.4881666666666666)
    def test_2(self):
        ''' Test sequence for '.5' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, .5), 1.284)
    def test_3(self):
        ''' Test sequence for '.49' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, .49), 1.27522)
    def test_4(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, 0), 1.)
    def test_5(self):
        ''' Test sequence for '.1' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, .1), 1.0101)
    def test_6(self):
        ''' Test sequence for '.01' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, .01), 1.00101)
    def test_7(self):
        ''' Test sequence for '1' '''
        self.assertAlmostEqual(self.unit.interpol(self.pos, self.val, 1), 2.7183)
    def test_8(self):
        ''' Test sequence for '1.1' '''
        self.assertTrue(self.unit.interpol(self.pos, self.val, 1.1) is nan)
    def test_9(self):
        ''' Test sequence for '-0.1' '''
        self.assertTrue(self.unit.interpol(self.pos, self.val, -.1) is nan)
if __name__ == '__main__':
    unittest.main()
