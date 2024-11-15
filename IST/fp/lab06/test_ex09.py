#! /usr/bin/env python3
''' tests for ex09.py '''
import unittest
from random import seed
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
        ''' Test sequence for '1001' '''
        seed(1001)
        self.assertEqual(self.unit.euromilhoes(), [[3, 5, 39, 40, 44], [10, 11]])
    def test_2(self):
        ''' Test sequence for '0' '''
        seed(0)
        self.assertEqual(self.unit.euromilhoes(), [[13, 22, 26, 38, 43], [5, 10]])
if __name__ == '__main__':
    unittest.main()
