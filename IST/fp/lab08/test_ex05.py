#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
SKIP = False
try :
    import ex05
except ImportError:
    SKIP = True
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex05.py")
        self.unit = ex05
    def test_inf(self):
        ''' Test sequence for '3, 5' '''
        cnt = self.unit.ContadorLimitado(3, 5)
        self.assertEqual(3, cnt.consulta())
    def test_sup(self):
        ''' Test sequence for '.inc()' '''
        cnt = self.unit.ContadorLimitado(3, 5)
        cnt.inc()
        cnt.inc()
        cnt.inc()
        cnt.inc()
        self.assertEqual(5, cnt.consulta())
    def test_middle(self):
        ''' Test sequence for '.inc() .dec()' '''
        cnt = self.unit.ContadorLimitado(3, 5)
        cnt.inc()
        cnt.dec()
        cnt.inc()
        cnt.dec()
        cnt.inc()
        self.assertEqual(4, cnt.consulta())
    def test_low(self):
        ''' Test sequence for '.dec()' '''
        cnt = self.unit.ContadorLimitado(3, 5)
        cnt.dec()
        self.assertEqual(3, cnt.consulta())
    def test_limite(self):
        ''' Test sequence for '5, 3' '''
        self.assertRaises(ValueError, self.unit.ContadorLimitado, 5, 3)
    def test_equal(self):
        ''' Test sequence for '3, 3' '''
        self.assertRaises(ValueError, self.unit.ContadorLimitado, 3, 3)
if __name__ == '__main__':
    unittest.main()
