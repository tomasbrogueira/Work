#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
    def test_1(self):
        ''' Test sequence for '.numero_digitos(9)' '''
        self.assertEqual(self.unit.numero_digitos(9), 1)
    def test_2(self):
        ''' Test sequence for '.numero_digitos(1012)' '''
        self.assertEqual(self.unit.numero_digitos(1012), 4)
    def test_3(self):
        ''' Test sequence for '.numero_digitos2(9)' '''
        self.assertEqual(self.unit.numero_digitos2(9), 1)
    def test_4(self):
        ''' Test sequence for '.numero_digitos2(1012)' '''
        self.assertEqual(self.unit.numero_digitos2(1012), 4)
    def test_5(self):
        ''' Test sequence for '.numero_digitos3(9)' '''
        self.assertEqual(self.unit.numero_digitos3(9), 1)
    def test_6(self):
        ''' Test sequence for '.numero_digitos3(1012)' '''
        self.assertEqual(self.unit.numero_digitos3(1012), 4)
if __name__ == '__main__':
    unittest.main()
