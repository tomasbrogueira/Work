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
        ''' Test sequence for '.filtra()' '''
        self.assertEqual(self.unit.filtra(lambda x : x % 2 == 0, [1, 2, 3, 4, 5]), [2, 4])
    def test_2(self):
        ''' Test sequence for '.transforma()' '''
        self.assertEqual(self.unit.transforma(lambda x : x ** 3, [1, 2, 3, 4]), [1, 8, 27, 64])
    def test_3(self):
        ''' Test sequence for '.acumula()' '''
        self.assertEqual(self.unit.acumula(lambda x, y : x + y, [1, 2, 3, 4]), 10)
if __name__ == '__main__':
    unittest.main()
