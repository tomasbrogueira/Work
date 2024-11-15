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
        ''' Test sequence for 'A1' '''
        self.assertTrue(self.unit.reconhece('A1'))
    def test_2(self):
        ''' Test sequence for 'ABBBBCDDDD23311' '''
        self.assertTrue(self.unit.reconhece('ABBBBCDDDD23311'))
    def test_3(self):
        ''' Test sequence for 'ABC12C' '''
        self.assertFalse(self.unit.reconhece('ABC12C'))
if __name__ == '__main__':
    unittest.main()
