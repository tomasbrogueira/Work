#! /usr/bin/env python3
''' tests for ex10.py '''
import unittest
SKIP = False
try :
    import ex10
except ImportError:
    SKIP = True
class TestEx10(unittest.TestCase):
    ''' test class for ex10.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex10.py")
        self.unit = ex10
    def test_1(self):
        ''' Test sequence for '1234567890' '''
        self.assertEqual(self.unit.apenas_digitos_impares(1234567890), 13579)
    def test_2(self):
        ''' Test sequence for '10' '''
        self.assertEqual(self.unit.apenas_digitos_impares(10), 1)
    def test_3(self):
        ''' Test sequence for '1000001' '''
        self.assertEqual(self.unit.apenas_digitos_impares(1000001), 11)
    def test_4(self):
        ''' Test sequence for '246898642' '''
        self.assertEqual(self.unit.apenas_digitos_impares(246898642), 9)
if __name__ == '__main__':
    unittest.main()
