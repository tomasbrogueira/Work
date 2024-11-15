#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
SKIP = False
try :
    import ex01
except ImportError:
    SKIP = True
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex01.py")
        self.unit = ex01
    def test_1(self):
        ''' Test sequence for '[2, 3, 5, 9, 12, 33, 34, 45], 3' '''
        self.assertEqual(self.unit.remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3), [2, 5, 34])
    def test_2(self):
        ''' Test sequence for '[1,2,3,4,5,6,7,8,9], 2' '''
        self.assertEqual(self.unit.remove_multiplos([1,2,3,4,5,6,7,8,9], 2), [1,3,5,7,9])
    def test_3(self):
        ''' Test sequence for '[1,2,3,4,5,6,7,8,9], 1' '''
        self.assertEqual(self.unit.remove_multiplos([1,2,3,4,5,6,7,8,9], 1), [])
    def test_4(self):
        ''' Test sequence for '[2, 3, 5, 9, 12, 33, 34, 45], 5' '''
        self.assertEqual(self.unit.remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 5),
            [2,3,9,12,33,34])
    def test_5(self):
        ''' Test sequence for '[], 3' '''
        self.assertEqual(self.unit.remove_multiplos([], 3), [])
    def test_6(self):
        ''' Test sequence for '[2, 3, 5, 9, 12, 33, 34, 45], 3' '''
        vals = [2, 3, 5, 9, 12, 33, 34, 45]
        self.unit.remove_multiplos(vals, 3)
        self.assertEqual(vals, [2, 5, 34])
if __name__ == '__main__':
    unittest.main()
