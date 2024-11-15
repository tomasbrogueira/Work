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
        with open("ex15.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '391' '''
        self.assertEqual(self.unit.espelho(391), 193)
    def test_2(self):
        ''' Test sequence for '45679' '''
        self.assertEqual(self.unit.espelho(45679), 97654)
    def test_3(self):
        ''' Test sequence for '1000' '''
        self.assertEqual(self.unit.espelho(1000), 1)
    def test_4(self):
        ''' Test sequence for '0' '''
        self.assertEqual(self.unit.espelho(0), 0)
if __name__ == '__main__':
    unittest.main()
