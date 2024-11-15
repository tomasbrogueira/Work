#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
SKIP = False
try :
    import ex17
except ImportError:
    SKIP = True
class TestEx17(unittest.TestCase):
    ''' test class for ex17.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex17.py")
        self.unit = ex17
    def test_1(self):
        ''' Test sequence for '2' '''
        func = self.unit.acumula([1, 2, 3])
        self.assertEqual(func(2), [3, 4, 5])
    def test_2(self):
        ''' Test sequence for '2, 4, -12' '''
        func = self.unit.acumula([1, 2, 3])
        func(2)
        func(4)
        self.assertEqual(func(-12), [-5, -4, -3])
    def test_3(self):
        ''' Test sequence for empty list '''
        func = self.unit.acumula([])
        self.assertEqual(func(4), [])
    def test_4(self):
        ''' Test sequence for reals '''
        lst = [1.2, 2.3, 3.4]
        func = self.unit.acumula(lst)
        func(4.5)
        self.assertEqual(len(lst), 3)
        self.assertAlmostEqual(lst[0], 5.7)
        self.assertAlmostEqual(lst[1], 6.8)
        self.assertAlmostEqual(lst[2], 7.9)
    def test_5(self):
        ''' Test sequence for '2, 4, -12' with real '''
        func = self.unit.acumula([1, 2, 3])
        self.assertEqual(func(3.4), [4.4, 5.4, 6.4])
if __name__ == '__main__':
    unittest.main()
