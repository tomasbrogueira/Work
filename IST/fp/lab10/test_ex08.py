#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
SKIP = False
try :
    import ex08
except ImportError:
    SKIP = True
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex08.py")
        self.unit = ex08
        with open("ex08.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[2, 3, 4, 5], [2, 3]' '''
        self.assertEqual(self.unit.subtrai([2, 3, 4, 5], [2, 3]), [4, 5])
    def test_2(self):
        ''' Test sequence for '[2, 3, 4, 5], [6, 7]' '''
        self.assertEqual(self.unit.subtrai([2, 3, 4, 5], [6, 7]), [2, 3, 4, 5])
if __name__ == '__main__':
    unittest.main()
