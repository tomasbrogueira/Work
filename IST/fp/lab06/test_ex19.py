#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        sys.stdout = StringIO()
        self.stdout = sys.stdout
        self.unit = ex19
    def tearDown(self):
        sys.stdout = self.stdout
    def test_1(self):
        ''' Test sequence for '4, 6' '''
        self.assertEqual(self.unit.cria_racional(4, 6), {'d': 3, 'n': 2})
    def test_2(self):
        ''' Test sequence for '4, 0' '''
        self.assertRaises(ValueError, self.unit.cria_racional, 4, 0)
    def test_3(self):
        ''' Test sequence for '4.3, 2' '''
        self.assertRaises(ValueError, self.unit.cria_racional, 4.3, 2)
    def test_4(self):
        ''' Test sequence for '{'d': 4, 'n': 6}' '''
        self.unit.escreve_racional({'d': 4, 'n': 6})
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "3/2\n")
    def test_5(self):
        ''' Test sequence for '.soma_racionais()' '''
        rat1 = {'d': 6, 'n': 4}
        rat2 = {'d': 3, 'n': 2}
        rat3 = {'d': 3, 'n': 4}
        self.assertEqual(self.unit.soma_racionais(rat1, rat2), rat3)
    def test_6(self):
        ''' Test sequence for '-4, 6' '''
        self.assertEqual(self.unit.cria_racional(-4, 6), {'d': 3, 'n': -2})
    def test_7(self):
        ''' Test sequence for '-4, -6' '''
        self.assertEqual(self.unit.cria_racional(-4, -6), {'d': 3, 'n': 2})
    def test_8(self):
        ''' Test sequence for '4, -6' '''
        self.assertEqual(self.unit.cria_racional(4, -6), {'d': 3, 'n': -2})
if __name__ == '__main__':
    unittest.main()
