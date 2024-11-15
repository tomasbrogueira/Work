#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        self.unit = ex19
    def test_1(self):
        ''' Test sequence for signle '''
        dic = {}
        func = self.unit.acrescenta(dic)
        self.assertEqual(func('a', 2), 1)
    def test_2(self):
        ''' Test sequence for multiple '''
        dic = {}
        func = self.unit.acrescenta(dic)
        func('a', 0)
        func('a', 1)
        self.assertEqual(func('a', 2), 3)
    def test_3(self):
        ''' Test sequence for existing '''
        dic = {'a': [ 3, 5, 7, 9 ], 'b': [12], 'c': [] }
        func = self.unit.acrescenta(dic)
        self.assertEqual(func('a', 2), 5)
        self.assertEqual(dic['a'], [ 3, 5, 7, 9, 2 ])
    def test_4(self):
        ''' Test sequence for empty '''
        dic = {'a': [ 3, 5, 7, 9 ], 'b': [12], 'c': [] }
        func = self.unit.acrescenta(dic)
        self.assertEqual(func('c', 2), 1)
        self.assertEqual(len(dic['c']), 1)
if __name__ == '__main__':
    unittest.main()
