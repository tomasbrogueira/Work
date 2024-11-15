#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
SKIP = False
try :
    import ex12
except ImportError:
    SKIP = True
class TestEx12(unittest.TestCase):
    ''' test class for ex12.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex12.py")
        self.unit = ex12
    def test_1(self):
        ''' Test sequence for '0, 3' '''
        func = self.unit.intervalo(0,3)
        self.assertFalse(func(8))
        self.assertTrue(func(2))
    def test_2(self):
        ''' Test sequence for '0, 12' '''
        func = self.unit.intervalo(0,12)
        self.assertFalse(func(13))
        self.assertTrue(func(2))
        self.assertTrue(func(0))
        self.assertTrue(func(12))
    def test_3(self):
        ''' Test sequence for '0, 0' '''
        func = self.unit.intervalo(0,0)
        self.assertFalse(func(1))
        self.assertTrue(func(0))
    def test_4(self):
        ''' Test sequence for '-2, 0' '''
        func = self.unit.intervalo(-2, 0)
        self.assertFalse(func(1))
        self.assertFalse(func(-3))
        self.assertTrue(func(0))
        self.assertTrue(func(-1))
        self.assertTrue(func(0))
if __name__ == '__main__':
    unittest.main()
