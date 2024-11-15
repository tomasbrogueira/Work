#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
SKIP = False
try :
    import ex11
except ImportError:
    SKIP = True
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex11.py")
        self.unit = ex11
    def test_0(self):
        ''' Test sequence for '0' '''
        self.assertAlmostEqual(self.unit.pi(0), 0)
    def test_1(self):
        ''' Test sequence for '1' '''
        self.assertAlmostEqual(self.unit.pi(1), 4)
    def test_2(self):
        ''' Test sequence for '2' '''
        self.assertAlmostEqual(self.unit.pi(2), 2.666666666666667)
    def test_20(self):
        ''' Test sequence for '20' '''
        self.assertAlmostEqual(self.unit.pi(20), 3.09162380666784)
    def test_200(self):
        ''' Test sequence for '200' '''
        self.assertAlmostEqual(self.unit.pi(200), 3.136592684838816)
    def test_2000(self):
        ''' Test sequence for '2000' '''
        self.assertAlmostEqual(self.unit.pi(2000), 3.1410926536210413)
    def test_20000(self):
        ''' Test sequence for '20000' '''
        self.assertAlmostEqual(self.unit.pi(20000), 3.1415426535898248)
if __name__ == '__main__':
    unittest.main()
