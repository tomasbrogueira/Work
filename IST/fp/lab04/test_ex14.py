#! /usr/bin/env python3
''' tests for ex14.py '''
import unittest
from math import exp, log
def func(_, pos):
    ''' Function to approximate '''
    return 2 * exp(-pos)
def sol(val):
    ''' Approximate solution to function '''
    return log(2*val+exp(2))
SKIP = False
try :
    import ex14
except ImportError:
    SKIP = True
class TestEx14(unittest.TestCase):
    ''' test class for ex14.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex14.py")
        self.unit = ex14
    def test_5(self):
        ''' Test sequence for '5' '''
        self.assertAlmostEqual(self.unit.euler(func, 2, 0, 1, 5), 2.244832660832381)
    def test_25(self):
        ''' Test sequence for '25' '''
        self.assertAlmostEqual(self.unit.euler(func, 2, 0, 1, 25), 2.2405724553626363)
    def test_500(self):
        ''' Test sequence for '500' '''
        self.assertAlmostEqual(self.unit.euler(func, 2, 0, 1, 500), 2.2395958103632485)
    def test_5000(self):
        ''' Test sequence for '5000' '''
        self.assertAlmostEqual(self.unit.euler(func, 2, 0, 1, 5000), 2.239549869037325)
    def test_600000(self):
        ''' Test sequence for '600000' '''
        self.assertAlmostEqual(self.unit.euler(func, 2, 0, 1, 600000), sol(1)) # takes .5secs
if __name__ == '__main__':
    unittest.main()
