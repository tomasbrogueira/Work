#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
SKIP = False
try :
    import ex16
except ImportError:
    SKIP = True
class TestEx16(unittest.TestCase):
    ''' test class for ex16.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex16.py")
        self.unit = ex16
    def test_1(self):
        ''' Test sequence for '(4,3,2), 1.2), 11.36' '''
        self.assertAlmostEqual(self.unit.horner((4,3,2), 1.2), 11.36)
    def test_2(self):
        ''' Test sequence for '(4,3,2), 0), 2' '''
        self.assertAlmostEqual(self.unit.horner((4,3,2), 0), 2)
    def test_3(self):
        ''' Test sequence for '(4,0,0), 1), 4' '''
        self.assertAlmostEqual(self.unit.horner((4,0,0), 1), 4)
    def test_4(self):
        ''' Test sequence for '(2,), 12), 2' '''
        self.assertAlmostEqual(self.unit.horner((2,), 12), 2)
    def test_5(self):
        ''' Test sequence for '(8,-3,-4,3,2,-4), 1.5), 37.8125' '''
        self.assertAlmostEqual(self.unit.horner((8,-3,-4,3,2,-4), 1.5), 37.8125)
    def test_6(self):
        ''' Test sequence for '(8,0,0,0,0,0,0,0,8), 2), 2056' '''
        self.assertAlmostEqual(self.unit.horner((8,0,0,0,0,0,0,0,8), 2), 2056)
    def test_7(self):
        ''' Test sequence for '(0,0,0), 162), 0' '''
        self.assertAlmostEqual(self.unit.horner((0,0,0), 162), 0)
    def test_8(self):
        ''' Test sequence for '(8,0,0,0,0,0,0,0,8), 1.1), 25.148710480000013' '''
        self.assertAlmostEqual(self.unit.horner((8,0,0,0,0,0,0,0,8), 1.1), 25.148710480000013)
if __name__ == '__main__':
    unittest.main()
