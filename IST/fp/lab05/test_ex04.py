#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
SKIP = False
try :
    import ex04
except ImportError:
    SKIP = True
class TestEx04(unittest.TestCase):
    ''' test class for ex04.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex04.py")
        self.unit = ex04
    def test_1(self):
        ''' Test sequence for '(2, 5, 6, 7, 9, 1, 8, 8)' '''
        self.assertEqual(self.unit.filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)), (2, 6, 8, 8))
    def test_2(self):
        ''' Test sequence for '(2, 8, 6, 8, 0, 4, 8, 8)' '''
        self.assertEqual(self.unit.filtra_pares((2, 8, 6, 8, 0, 4, 8, 8)), (2, 8, 6, 8, 0, 4, 8, 8))
    def test_3(self):
        ''' Test sequence for '(1, 5, 9, 7, 9, 1, 3, 11)' '''
        self.assertEqual(self.unit.filtra_pares((1, 5, 9, 7, 9, 1, 3, 11)), ())
    def test_4(self):
        ''' Test sequence for '()' '''
        self.assertEqual(self.unit.filtra_pares(()), ())
if __name__ == '__main__':
    unittest.main()
