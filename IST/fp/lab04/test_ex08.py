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
    def test_2(self):
        ''' Test sequence for '2' '''
        self.assertAlmostEqual(self.unit.area_circulo(2), 12.566370614359172)
    def test_5(self):
        ''' Test sequence for '5' '''
        self.assertAlmostEqual(self.unit.area_circulo(5), 78.53981633974483)
    def test_10(self):
        ''' Test sequence for '10' '''
        self.assertAlmostEqual(self.unit.area_circulo(10), 314.1592653589793)
    def test_0(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.area_circulo(0), 0.)
    def test_2_38(self):
        ''' Test sequence for '2.38' '''
        self.assertAlmostEqual(self.unit.area_circulo(2.38), 17.795237426994024)
    def test__2(self):
        ''' Test sequence for '-2' '''
        self.assertAlmostEqual(self.unit.area_circulo(-2), 0.)
if __name__ == '__main__':
    unittest.main()
