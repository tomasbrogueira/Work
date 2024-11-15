#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
SKIP = False
try :
    import ex05
except ImportError:
    SKIP = True
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex05.py")
        self.unit = ex05
    def test_1(self):
        ''' Test sequence for '6643399766641' '''
        self.assertEqual(self.unit.algarismos_pares(6643399766641), 6646664)
    def test_2(self):
        ''' Test sequence for '664866640' '''
        self.assertEqual(self.unit.algarismos_pares(664866640), 664866640)
    def test_3(self):
        ''' Test sequence for '3399751' '''
        self.assertEqual(self.unit.algarismos_pares(3399751), 0)
    def test_4(self):
        ''' Test sequence for '0' '''
        self.assertRaises(ValueError, self.unit.algarismos_pares, 0)
if __name__ == '__main__':
    unittest.main()
