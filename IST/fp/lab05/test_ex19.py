#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
from statistics import variance
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
        ''' Test sequence for '(1.0, 1.0101, 1.0645, 1.284, 1.8965, 2.7183)' '''
        val = (1.0, 1.0101, 1.0645, 1.284, 1.8965, 2.7183)
        self.assertAlmostEqual(self.unit.variance(val), variance(val))
    def test_2(self):
        ''' Test sequence for '( 1., 1.0645, 1.2840, 1.7551, 2.7183 )' '''
        val = ( 1., 1.0645, 1.2840, 1.7551, 2.7183 )
        self.assertAlmostEqual(self.unit.variance(val), variance(val))
    def test_3(self):
        ''' Test sequence for '( 3, ) * 12' '''
        val = ( 3, ) * 12
        self.assertAlmostEqual(self.unit.variance(val), variance(val))
    def test_4(self):
        ''' Test sequence for '( -12, ) * 3 + ( 12, ) * 3' '''
        val = ( -12, ) * 3 + ( 12, ) * 3
        self.assertAlmostEqual(self.unit.variance(val), variance(val))
    def test_5(self):
        ''' Test sequence for 'range(8)' '''
        val = range(8)
        self.assertAlmostEqual(self.unit.variance(val), variance(val))
if __name__ == '__main__':
    unittest.main()
