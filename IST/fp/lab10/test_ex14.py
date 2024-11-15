#! /usr/bin/env python3
''' tests for ex14.py '''
import unittest
SKIP = False
try :
    import ex14
except ImportError:
    SKIP = True
class TestEx14(unittest.TestCase):
    ''' test class for ex14.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex14.py")
        self.unit = ex14
        with open("ex14.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '12321' '''
        self.assertTrue(self.unit.eh_capicua(12321))
    def test_2(self):
        ''' Test sequence for '1221' '''
        self.assertTrue(self.unit.eh_capicua(1221))
    def test_3(self):
        ''' Test sequence for '123210' '''
        self.assertFalse(self.unit.eh_capicua(123210))
if __name__ == '__main__':
    unittest.main()
