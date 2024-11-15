#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
SKIP = False
try :
    import ex12
except ImportError:
    SKIP = True
class TestEx12(unittest.TestCase):
    ''' test class for ex12.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex12.py")
        self.unit = ex12
    def test_1(self):
        ''' Test sequence for '.quadrado(12)' '''
        self.assertEqual(self.unit.quadrado(12), 144)
    def test_2(self):
        ''' Test sequence for '.quadrado(3)' '''
        self.assertEqual(self.unit.quadrado(3), 9)
    def test_3(self):
        ''' Test sequence for '.quadrado2(12)' '''
        self.assertEqual(self.unit.quadrado2(12), 144)
    def test_4(self):
        ''' Test sequence for '.quadrado2(3)' '''
        self.assertEqual(self.unit.quadrado2(3), 9)
    def test_5(self):
        ''' Test sequence for '.quadrado3(12)' '''
        self.assertEqual(self.unit.quadrado3(12), 144)
    def test_6(self):
        ''' Test sequence for '.quadrado3(3)' '''
        self.assertEqual(self.unit.quadrado3(3), 9)
if __name__ == '__main__':
    unittest.main()
