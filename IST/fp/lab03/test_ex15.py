#! /usr/bin/env python3
''' tests for ex15.py '''
import unittest
SKIP = False
try :
    import ex15
except ImportError:
    SKIP = True
class TestEx15(unittest.TestCase):
    ''' test class for ex15.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex15.py")
        self.unit = ex15
    def test_0(self):
        ''' Test sequence with number 0 '''
        self.assertFalse(self.unit.cinco(0))
    def test_4(self):
        ''' Test sequence with number 4 '''
        self.assertFalse(self.unit.cinco(4))
    def test_5(self):
        ''' Test sequence with number 5 '''
        self.assertTrue(self.unit.cinco(5))
    def test_6(self):
        ''' Test sequence with number 6 '''
        self.assertFalse(self.unit.cinco(6))
    def test_12(self):
        ''' Test sequence with number 12 '''
        self.assertFalse(self.unit.cinco(12))
if __name__ == '__main__':
    unittest.main()
