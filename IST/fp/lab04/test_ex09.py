#! /usr/bin/env python3
''' tests for ex09.py '''
import unittest
SKIP = False
try :
    import ex09
except ImportError:
    SKIP = True
class TestEx09(unittest.TestCase):
    ''' test class for ex09.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex09.py")
        self.unit = ex09
    def test_12_13(self):
        ''' Test sequence for '12 13' '''
        self.assertAlmostEqual(self.unit.area_coroa(12, 13), 78.53981633974485)
    def test_12_10(self):
        ''' Test sequence for '12 10' '''
        self.assertRaises(ValueError, self.unit.area_coroa, 12, 10)
    def test_1_2(self):
        ''' Test sequence for '1 2' '''
        self.assertAlmostEqual(self.unit.area_coroa(1, 2), 9.42477796076938)
    def test_0_2(self):
        ''' Test sequence for '0 2' '''
        self.assertAlmostEqual(self.unit.area_coroa(0, 2), 12.566370614359172)
    def test_0_0(self):
        ''' Test sequence for '0 0' '''
        self.assertAlmostEqual(self.unit.area_coroa(0, 0), 0.)
    def test_99_100(self):
        ''' Test sequence for '99 100' '''
        self.assertAlmostEqual(self.unit.area_coroa(99, 100), 625.1769380643709)
    def test__5__2(self):
        ''' Test sequence for '-5 -2' '''
        self.assertAlmostEqual(self.unit.area_coroa(-5, -2), 0.)
    def test___2__5(self):
        ''' Test sequence for '-2 -5' '''
        self.assertRaises(ValueError, self.unit.area_coroa, -2, -5)
if __name__ == '__main__':
    unittest.main()
