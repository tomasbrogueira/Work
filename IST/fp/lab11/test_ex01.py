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
        ''' Test sequence for '9, 21' '''
        self.assertEqual(self.unit.somatorio(9, 21, lambda x : x * x,
            lambda x : x + 3), 1215)
    def test_2(self):
        ''' Test sequence for '4, 500' '''
        self.assertEqual(self.unit.somatorio(4, 500, lambda x: x,
            lambda x: x + 1), 125244)
    def test_3(self):
        ''' Test sequence for '5, 500' '''
        self.assertEqual(self.unit.somatorio(5, 500, lambda x: x * x,
            lambda x: x + 5), 8458750)
    def test_4(self):
        ''' Test sequence for '1 5' '''
        self.assertEqual(self.unit.somatorio(1, 5,
            lambda x: self.unit.somatorio(1, x, lambda x: x, lambda x: x+1),
            lambda x: x+1), 35)
if __name__ == '__main__':
    unittest.main()
