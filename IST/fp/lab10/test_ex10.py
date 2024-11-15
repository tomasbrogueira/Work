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
        with open("ex10.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[5, 3, 8, 1, 9, 2]' '''
        self.assertEqual(self.unit.maior([5, 3, 8, 1, 9, 2]), 9)
    def test_2(self):
        ''' Test sequence for '[-5, -3, -8, -1, -9, -2]' '''
        self.assertEqual(self.unit.maior([-5, -3, -8, -1, -9, -2]), -1)
    def test_3(self):
        ''' Test sequence for '[9, 3, 8, 1, 5, 2]' '''
        self.assertEqual(self.unit.maior([9, 3, 8, 1, 5, 2]), 9)
    def test_4(self):
        ''' Test sequence for '[5, 3, 8, 1, 2, 9]' '''
        self.assertEqual(self.unit.maior([5, 3, 8, 1, 2, 9]), 9)
if __name__ == '__main__':
    unittest.main()
