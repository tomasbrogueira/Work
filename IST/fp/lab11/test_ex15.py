#! /usr/bin/env python3
''' tests for ex15.py '''
import unittest
SKIP = False
try :
    import ex15
except ImportError:
    SKIP = True
class TestEx15(unittest.TestCase):
    ''' test class for ex15.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex15.py")
        self.unit = ex15
    def test_1(self):
        ''' Test sequence for '11' '''
        func = self.unit.index([3, 5, 7, 9, 11, 17])
        self.assertEqual(func(11), 4)
    def test_2(self):
        ''' Test sequence for '4' '''
        func = self.unit.index([3, 5, 7, 9, 11, 17])
        self.assertEqual(func(4), -1)
    def test_3(self):
        ''' Test sequence for '5' '''
        func = self.unit.index([3, 5, 7, 9, 5, 3])
        self.assertEqual(func(5), 1)
    def test_4(self):
        ''' Test sequence for reals '''
        func = self.unit.index([1.2, 3.1, 4.3])
        self.assertEqual(func(4.3), 2)
    def test_5(self):
        ''' Test sequence for strings '''
        func = self.unit.index(['abc', 'def', 'hij'])
        self.assertEqual(func('def'), 1)
    def test_6(self):
        ''' Test sequence for multiple types '''
        func = self.unit.index([1.2, 'def', ()])
        self.assertEqual(func(tuple()), 2)
    def test_7(self):
        ''' Test sequence for empty list '''
        func = self.unit.index([])
        self.assertEqual(func(4.3), -1)
        self.assertEqual(func('def'), -1)
        self.assertEqual(func(None), -1)
        self.assertEqual(func([]), -1)
if __name__ == '__main__':
    unittest.main()
