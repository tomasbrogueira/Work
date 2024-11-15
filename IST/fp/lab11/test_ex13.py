#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
    def test_1(self):
        ''' Test sequence for '3' '''
        func = self.unit.tabuada(3)
        self.assertEqual(func(8), 24)
    def test_2(self):
        ''' Test sequence for '12' '''
        func = self.unit.tabuada(12)
        self.assertEqual(func(8), 8*12)
        self.assertEqual(func(20), 12*20)
    def test_3(self):
        ''' Test sequence for '0' '''
        func = self.unit.tabuada(0)
        self.assertEqual(func(8), 0)
    def test_4(self):
        ''' Test sequence for '-2' '''
        func = self.unit.tabuada(-2)
        self.assertEqual(func(8), 8*-2)
if __name__ == '__main__':
    unittest.main()
