#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
from math import exp, cos
def func(val):
    ''' Test functions for tests '''
    return val + exp(-val) -2
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
    def test_20(self):
        ''' Test sequence for 'func' in [0, 2] '''
        res = self.unit.bissecao(func, 0, 2)
        self.assertAlmostEqual(res[0], 1.8414058685302734)
        self.assertEqual(res[1], 20)
    def test_1_3(self):
        ''' Test sequence for 'func' in [1.3, 2] '''
        res = self.unit.bissecao(func, 1.3, 2)
        self.assertAlmostEqual(res[0], 1.84140625)
        self.assertAlmostEqual(res[1], 7)
    def test_200(self):
        ''' Test sequence for 'func' in [-1, 200] '''
        res = self.unit.bissecao(func, -1, 200)
        self.assertAlmostEqual(res[0], 1.8414051830768585)
        self.assertAlmostEqual(res[1], 25)
    def test_cos(self):
        ''' Test sequence for 'cos' '''
        res = self.unit.bissecao(cos, 1, 3)
        self.assertAlmostEqual(res[0], 1.5707969665527344)
        self.assertAlmostEqual(res[1], 19)
    def test_feps_neps(self):
        ''' Test sequence for 'cos' with 'feps' and 'neps' '''
        res = self.unit.bissecao(cos, 1, 3, feps=1e-15, neps=1e-12)
        self.assertAlmostEqual(res[0], 1.5707963267950618)
        self.assertAlmostEqual(res[1], 41)
    def test_raise(self):
        ''' Test sequence for ValueError '''
        self.assertRaises(ValueError, self.unit.bissecao, func, 0, 1)
if __name__ == '__main__':
    unittest.main()
