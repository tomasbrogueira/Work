#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
SKIP = False
try :
    import ex05
except ImportError:
    SKIP = True
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex05.py")
        self.unit = ex05
    def test_1(self):
        ''' Test sequence for '[1,2,3,4,5,6]' '''
        self.assertEqual(self.unit.soma_quadrados_impares([1,2,3,4,5,6]), 35)
    def test_2(self):
        ''' Test sequence for '[1,3,5]' '''
        self.assertEqual(self.unit.soma_quadrados_impares([1,3,5]), 35)
    def test_3(self):
        ''' Test sequence for '[1,2,4,6]' '''
        self.assertEqual(self.unit.soma_quadrados_impares([1,2,4,6]), 1)
    def test_4(self):
        ''' Test sequence for '[2,4,5,6]' '''
        self.assertEqual(self.unit.soma_quadrados_impares([2,4,5,6]), 25)
if __name__ == '__main__':
    unittest.main()
