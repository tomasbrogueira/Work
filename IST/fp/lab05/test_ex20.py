#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
        self.pos = (0, 0.1, 0.25, 0.5, 0.8, 1.0)
    def test_1(self):
        ''' Test sequence for '0.1' '''
        self.assertEqual(self.unit.closest(self.pos, .1), .1)
    def test_2(self):
        ''' Test sequence for '0.01' '''
        self.assertEqual(self.unit.closest(self.pos, .01), 0)
    def test_3(self):
        ''' Test sequence for '0.051' '''
        self.assertEqual(self.unit.closest(self.pos, .051), .1)
    def test_4(self):
        ''' Test sequence for '0.049' '''
        self.assertEqual(self.unit.closest(self.pos, .049), 0)
    def test_5(self):
        ''' Test sequence for '-12' '''
        self.assertEqual(self.unit.closest(self.pos, -12), 0)
    def test_6(self):
        ''' Test sequence for '12' '''
        self.assertEqual(self.unit.closest(self.pos, 12), 1.)
if __name__ == '__main__':
    unittest.main()
