#! /usr/bin/env python3
''' tests for ex10.py '''
import unittest
SKIP = False
try :
    import ex10
except ImportError:
    SKIP = True
class TestEx10(unittest.TestCase):
    ''' test class for ex10.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex10.py")
        self.unit = ex10
    def test_valor100(self):
        ''' Test sequence for '100 0.03 4' '''
        self.assertAlmostEqual(self.unit.valor(100, 0.03, 4), 112.55088100000002)
    def test_valor10(self):
        ''' Test sequence for '10 0.03 4' '''
        self.assertAlmostEqual(self.unit.valor(10, 0.03, 4), 11.255088100000002)
    def test_valor_07(self):
        ''' Test sequence for '10 0.07 4' '''
        self.assertAlmostEqual(self.unit.valor(10, 0.07, 4), 13.107960100000003)
    def test_valor__8(self):
        ''' Test sequence for '10 0.07 8' '''
        self.assertAlmostEqual(self.unit.valor(10, 0.07, 8), 17.181861798319208)
    def test_duplicar100(self):
        ''' Test sequence for '100 0.03' '''
        self.assertEqual(self.unit.duplicar(100, 0.03), 24)
    def test_duplicar10(self):
        ''' Test sequence for '10 0.07' '''
        self.assertEqual(self.unit.duplicar(10, 0.07), 11)
if __name__ == '__main__':
    unittest.main()
