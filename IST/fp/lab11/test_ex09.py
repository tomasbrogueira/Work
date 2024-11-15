#! /usr/bin/env python3
''' tests for ex09.py '''
import unittest
SKIP = False
try :
    import ex09
except ImportError:
    SKIP = True
class TestEx09(unittest.TestCase):
    ''' test class for ex09.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex09.py")
        self.unit = ex09
    def test_1(self):
        ''' Test sequence for 'x > 3' '''
        self.assertEqual(self.unit.produto_digitos(12345, lambda x : x > 3), 20)
    def test_2(self):
        ''' Test sequence for 'x' '''
        self.assertEqual(self.unit.produto_digitos(11111, lambda x : x), 1)
    def test_3(self):
        ''' Test sequence for 'x <= 3' '''
        self.assertEqual(self.unit.produto_digitos(12345, lambda x : x <= 3), 6)
    def test_4(self):
        ''' Test sequence for 'x % 2' '''
        self.assertEqual(self.unit.produto_digitos(12345, lambda x : x % 2), 15)
if __name__ == '__main__':
    unittest.main()
