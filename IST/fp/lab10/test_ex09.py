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
        with open("ex09.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[3, 5, 1, 4, 5, 8, 9], 4' '''
        self.assertEqual(self.unit.parte([3, 5, 1, 4, 5, 8, 9], 4), [[3, 1], [5, 4, 5, 8, 9]])
    def test_2(self):
        ''' Test sequence for '[3, 5, 1, 4, 5, 8, 9], 0' '''
        self.assertEqual(self.unit.parte([3, 5, 1, 4, 5, 8, 9], 0), [[], [3, 5, 1, 4, 5, 8, 9]])
    def test_3(self):
        ''' Test sequence for '[3, 5, 1, 4, 5, 8, 9], 10' '''
        self.assertEqual(self.unit.parte([3, 5, 1, 4, 5, 8, 9], 10), [[3, 5, 1, 4, 5, 8, 9], []])
    def test_4(self):
        ''' Test sequence for '[3, 5, 1, 4, 5, 8, 9], 5' '''
        self.assertEqual(self.unit.parte([3, 5, 1, 4, 5, 8, 9], 5), [[3, 1, 4], [5, 5, 8, 9]])
if __name__ == '__main__':
    unittest.main()
