#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
SKIP = False
try :
    import ex07
except ImportError:
    SKIP = True
class TestEx07(unittest.TestCase):
    ''' test class for ex07.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex07.py")
        self.unit = ex07
    def test_1(self):
        ''' Test sequence for '5467829' '''
        self.assertEqual(self.unit.filtra_pares(5467829), 4682)
    def test_2(self):
        ''' Test sequence for '4682' '''
        self.assertEqual(self.unit.filtra_pares(4682), 4682)
    def test_3(self):
        ''' Test sequence for '579' '''
        self.assertEqual(self.unit.filtra_pares(579), 0)
if __name__ == '__main__':
    unittest.main()