#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
    def test_1(self):
        ''' Test sequence for 'b' to 'x' '''
        dic = {'a':1, 'b':2, 'c':3}
        func = self.unit.substitui(dic)
        self.assertEqual(func('b', 'x'), 2)
        self.assertTrue('x' in dic)
        self.assertFalse('b' in dic)
        self.assertEqual(len(dic), 3)
    def test_2(self):
        ''' Test sequence for all to 'c' '''
        dic = {'a':1, 'b':2, 'c':3}
        func = self.unit.substitui(dic)
        func('a', 'b')
        self.assertEqual(func('b', 'c'), 1)
        self.assertEqual(len(dic), 1)
    def test_3(self):
        ''' Test sequence for reverse '''
        dic = {'a':1, 'b':2, 'c':3}
        func = self.unit.substitui(dic)
        func('a', 'x')
        self.assertEqual(func('x', 'a'), 1)
        self.assertEqual(len(dic), 3)
if __name__ == '__main__':
    unittest.main()
