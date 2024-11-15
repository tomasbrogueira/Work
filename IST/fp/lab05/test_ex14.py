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
    def test_1(self):
        ''' Test sequence for 'LaTeX' '''
        self.assertEqual(self.unit.minusculas("LaTeX"), "latex")
    def test_2(self):
        ''' Test sequence for 'latex' '''
        self.assertEqual(self.unit.minusculas("latex"), "latex")
    def test_3(self):
        ''' Test sequence for 'LATEX' '''
        self.assertEqual(self.unit.minusculas("LATEX"), "latex")
    def test_4(self):
        ''' Test sequence for '0_?#! ~:' '''
        self.assertEqual(self.unit.minusculas("0_?#! ~:"), "0_?#! ~:")
    def test_5(self):
        ''' Test sequence for 'El Rei Dom João' '''
        self.assertEqual(self.unit.minusculas("El Rei Dom João"), "el rei dom joão")
    def test_6(self):
        ''' Test sequence for 'EL REI DOM JOÃO' '''
        self.assertEqual(self.unit.minusculas("EL REI DOM JOÃO"), "el rei dom joão")
if __name__ == '__main__':
    unittest.main()
