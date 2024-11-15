#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
SKIP = False
try :
    import ex11
except ImportError:
    SKIP = True
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex11.py")
        self.unit = ex11
    def test_1(self):
        ''' Test sequence for '3' '''
        func = self.unit.incrementa(3)
        self.assertEqual(func(8), 11)
    def test_2(self):
        ''' Test sequence for '12' '''
        func = self.unit.incrementa(12)
        self.assertEqual(func(8), 20)
        self.assertEqual(func(20), 32)
    def test_3(self):
        ''' Test sequence for '0' '''
        func = self.unit.incrementa(0)
        self.assertEqual(func(8), 8)
    def test_4(self):
        ''' Test sequence for '-2' '''
        func = self.unit.incrementa(-2)
        self.assertEqual(func(8), 6)
if __name__ == '__main__':
    unittest.main()
