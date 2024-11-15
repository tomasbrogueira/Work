#! /usr/bin/env python3
''' tests for ex14.py '''
import unittest
SKIP = False
try :
    import ex14
except ImportError:
    SKIP = True
class TestEx14(unittest.TestCase):
    ''' test class for ex14.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex14.py")
        self.unit = ex14
    def test_1(self):
        ''' Test sequence for '34' '''
        func = self.unit.polinomio(12, 3, 4)
        self.assertEqual(func(2), 34)
    def test_2(self):
        ''' Test sequence for '3.4' '''
        func = self.unit.polinomio(12, 3, 4)
        self.assertAlmostEqual(func(3.4), 68.44)
    def test_3(self):
        ''' Test sequence for '-12, 3, 0' '''
        func = self.unit.polinomio(-12, 3, 0)
        self.assertEqual(func(4), 0)
        self.assertEqual(func(0), -12)
    def test_4(self):
        ''' Test sequence for reals '''
        func = self.unit.polinomio(1.2, 3.1, 4.3)
        self.assertAlmostEqual(func(8.7), 353.637)
        self.assertAlmostEqual(func(8), 301.2)
        self.assertAlmostEqual(func(5.7), 158.577)
if __name__ == '__main__':
    unittest.main()
