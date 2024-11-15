#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
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
    def test_2_4(self):
        ''' Test sequence with numbers 2, 4 '''
        self.assertEqual(self.unit.serie_geom(2, 4), 31)
    def test_100_0(self):
        ''' Test sequence with numbers 100, 0 '''
        self.assertEqual(self.unit.serie_geom(100, 0), 1)
    def test_4_2(self):
        ''' Test sequence with numbers 4, 2 '''
        self.assertEqual(self.unit.serie_geom(4, 2), 21)
    def test_12_8(self):
        ''' Test sequence with numbers 12, 8 '''
        self.assertEqual(self.unit.serie_geom(12, 8), 469070941)
    def test_3_12(self):
        ''' Test sequence with numbers 3, 12 '''
        self.assertEqual(self.unit.serie_geom(3, 12), 797161)
    def test_raise(self):
        ''' Test sequence with negative numbers '''
        self.assertRaises(ValueError, self.unit.serie_geom, 100, -1)
if __name__ == '__main__':
    unittest.main()
