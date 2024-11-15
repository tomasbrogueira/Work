#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
from random import randint
SKIP = False
try :
    import ex06
except ImportError:
    SKIP = True
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex06.py")
        self.unit = ex06
        with open("ex06.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[3, 4, 7, 9]' '''
        self.assertEqual(self.unit.inverte([3, 4, 7, 9]), [9, 7, 4, 3])
    def test_2(self):
        ''' Test sequence for 'range(100)' '''
        seq = [randint(1,999) for i in range(100)]
        self.assertEqual(self.unit.inverte(seq), seq[::-1])
if __name__ == '__main__':
    unittest.main()
