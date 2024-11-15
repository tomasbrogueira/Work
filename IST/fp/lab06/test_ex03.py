#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
SKIP = False
try :
    import ex03
except ImportError:
    SKIP = True
class TestEx03(unittest.TestCase):
    ''' test class for ex03.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex03.py")
        self.unit = ex03
    def test_1(self):
        ''' Test sequence for '[[1, 2, 3], [4, 5, 6]], 0, 0' '''
        self.assertEqual(self.unit.elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 0), 1)
    def test_2(self):
        ''' Test sequence for '[[1, 2, 3], [4, 5, 6]], 1, 2' '''
        self.assertEqual(self.unit.elemento_matriz([[1, 2, 3], [4, 5, 6]], 1, 2), 6)
    def test_3(self):
        ''' Test sequence for '[[1, 2, 3], [4, 5, 6]], 1, 0' '''
        self.assertEqual(self.unit.elemento_matriz([[1, 2, 3], [4, 5, 6]], 1, 0), 4)
    def test_4(self):
        ''' Test sequence for '[[1, 2, 3], [4, 5, 6]], 2, 1' '''
        self.assertRaises(ValueError, self.unit.elemento_matriz,[[1, 2, 3], [4, 5, 6]], 2, 1)
    def test_5(self):
        ''' Test sequence for '[], 0, 0' '''
        self.assertRaises(ValueError, self.unit.elemento_matriz,[], 0, 0)
    def test_6(self):
        ''' Test sequence for '[[], []], 0, 0' '''
        self.assertRaises(ValueError, self.unit.elemento_matriz,[[], []], 0, 0)
if __name__ == '__main__':
    unittest.main()
