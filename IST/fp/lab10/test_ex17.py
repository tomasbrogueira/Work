#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
SKIP = False
try :
    import ex17
except ImportError:
    SKIP = True
class TestEx17(unittest.TestCase):
    ''' test class for ex17.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex17.py")
        self.unit = ex17
        with open("ex17.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '1.2, 20' '''
        self.assertAlmostEqual(self.unit.calc_soma(1.2, 20), 3.3201169227365472)
    def test_2(self):
        ''' Test sequence for '5, 20' '''
        self.assertAlmostEqual(self.unit.calc_soma(5, 20), 148.41314706738183)
    def test_3(self):
        ''' Test sequence for '0, 10' '''
        self.assertAlmostEqual(self.unit.calc_soma(0, 10), 1.)
    def test_4(self):
        ''' Test sequence for '144, 200' '''
        self.assertAlmostEqual(self.unit.calc_soma(144, 200), 3.454646173557616e+62)
if __name__ == '__main__':
    unittest.main()
