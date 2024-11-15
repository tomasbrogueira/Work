#! /usr/bin/env python3
''' tests for ex21.py '''
import unittest
SKIP = False
try :
    import ex21
except ImportError:
    SKIP = True
class TestEx21(unittest.TestCase):
    ''' test class for ex21.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex21.py")
        self.unit = ex21
    def test_27983(self):
        ''' Test sequence with number 27983 '''
        self.assertEqual(self.unit.divisores(27983), 0)
    def test_30(self):
        ''' Test sequence with number 30 '''
        self.assertEqual(self.unit.divisores(30), 6)
    def test_144(self):
        ''' Test sequence with number 144 '''
        self.assertEqual(self.unit.divisores(144), 13)
    def test_120(self):
        ''' Test sequence with number 120 '''
        self.assertEqual(self.unit.divisores(120), 14)
    def test_12(self):
        ''' Test sequence with number 12 '''
        self.assertEqual(self.unit.divisores(12), 4)
    def test_neg(self):
        ''' Test sequence with negativenumber '''
        self.assertRaises(ValueError, self.unit.divisores, -12)
    def test_raise(self):
        ''' Test sequence with floating number '''
        self.assertRaises(ValueError, self.unit.divisores, 1.)
if __name__ == '__main__':
    unittest.main()
