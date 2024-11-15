#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
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
        ''' Test sequence for '1.4906875' output '''
        pos = ( 0., .25, .5, .75, 1. )
        val = ( 1., 1.0645, 1.2840, 1.7551, 2.7183 )
        self.assertAlmostEqual(self.unit.trapz(pos, val), 1.4906875)
    def test_2(self):
        ''' Test sequence for '1.4882175' output '''
        pos = ( 0, .1, .25, .5, .8, 1. )
        val = ( 1., 1.0101, 1.0645, 1.284, 1.8965, 2.7183 )
        self.assertAlmostEqual(self.unit.trapz(pos, val), 1.4882175)
if __name__ == '__main__':
    unittest.main()
