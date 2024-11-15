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
        ''' Test sequence for '3, 4' '''
        func = self.unit.segment([3, 4])
        func(3)
        func(2)
        self.assertEqual(func(6), [2,6])
    def test_2(self):
        ''' Test sequence for '3, 3' '''
        func = self.unit.segment([3, 3])
        self.assertEqual(func(3), [3,3])
    def test_3(self):
        ''' Test sequence for '0, 1' '''
        func = self.unit.segment([0, 1])
        func(3)
        func(-2)
        self.assertEqual(func(6), [-2,6])
    def test_4(self):
        ''' Test sequence for no list '''
        self.assertRaises(ValueError, self.unit.segment, (2,3))
    def test_5(self):
        ''' Test sequence for empty list '''
        self.assertRaises(ValueError, self.unit.segment, [])
    def test_6(self):
        ''' Test sequence for inverted list '''
        self.assertRaises(ValueError, self.unit.segment, [3, 2])
    def test_7(self):
        ''' Test sequence for short list '''
        self.assertRaises(ValueError, self.unit.segment, [3])
    def test_8(self):
        ''' Test sequence for long list '''
        self.assertRaises(ValueError, self.unit.segment, [3, 4, 5])
if __name__ == '__main__':
    unittest.main()
