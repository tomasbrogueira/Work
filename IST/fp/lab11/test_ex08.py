#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
SKIP = False
try :
    import ex08
except ImportError:
    SKIP = True
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex08.py")
        self.unit = ex08
    def test_1(self):
        ''' Test sequence for '123' '''
        self.assertEqual(self.unit.lista_digitos(123), [1, 2, 3])
    def test_0(self):
        ''' Test sequence for '0' '''
        self.assertEqual(self.unit.lista_digitos(0), [0])
if __name__ == '__main__':
    unittest.main()
