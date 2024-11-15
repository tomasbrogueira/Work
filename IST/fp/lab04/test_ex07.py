#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
SKIP = False
try :
    import ex07
except ImportError:
    SKIP = True
class TestEx07(unittest.TestCase):
    ''' test class for ex07.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex07.py")
        self.unit = ex07
    def test_48(self):
        ''' Test sequence for '48' '''
        self.assertAlmostEqual(self.unit.horas_dias(48), 2.)
    def test_10(self):
        ''' Test sequence for '10' '''
        self.assertAlmostEqual(self.unit.horas_dias(10), 10./24)
if __name__ == '__main__':
    unittest.main()
