#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
SKIP = False
try :
    import ex16
except ImportError:
    SKIP = True
class TestEx16(unittest.TestCase):
    ''' test class for ex16.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex16.py")
        self.unit = ex16
        with open("ex16.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '3' '''
        self.assertEqual(self.unit.g__(3), 2)
    def test_2(self):
        ''' Test sequence for '4' '''
        self.assertEqual(self.unit.g__(4), 3)
    def test_3(self):
        ''' Test sequence for '5' '''
        self.assertEqual(self.unit.g__(5), 3)
    def test_4(self):
        ''' Test sequence for '15' '''
        self.assertEqual(self.unit.g__(15), 9)
    def test_5(self):
        ''' Test sequence for '21' '''
        self.assertEqual(self.unit.g__(21), 13)
if __name__ == '__main__':
    unittest.main()
