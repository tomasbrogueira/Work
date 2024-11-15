#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
p100 = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27,
    28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50,
    51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72,
    74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93,
    94, 95, 96, 98, 99, 100]
SKIP = False
try :
    import ex06
except ImportError:
    SKIP = True
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex06.py")
        self.unit = ex06
    def test_1(self):
        ''' Test sequence for '10' '''
        self.assertEqual(self.unit.nao_primos(10), [1, 4, 6, 8, 9, 10])
    def test_2(self):
        ''' Test sequence for '1' '''
        self.assertEqual(self.unit.nao_primos(1), [1])
    def test_3(self):
        ''' Test sequence for '100' '''
        self.assertEqual(self.unit.nao_primos(100), p100)
if __name__ == '__main__':
    unittest.main()
