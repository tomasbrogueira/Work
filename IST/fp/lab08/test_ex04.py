#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex04
except ImportError:
    SKIP = True
class TestEx04(unittest.TestCase):
    ''' test class for ex04.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex04.py")
        self.unit = ex04
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_repr(self):
        ''' Test sequence for '20, 15, 50' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(repr(rel), "20:15:50")
    def test_hora(self):
        ''' Test sequence for '20, 15, 50' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel.obter_horas(), 20)
    def test_min(self):
        ''' Test sequence for '20, 15, 50' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel.obter_minutos(), 15)
    def test_seg(self):
        ''' Test sequence for '20, 15, 50' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel.obter_segundos(), 50)
    def test_mais_cedo(self):
        ''' Test sequence for '20, 15, 50' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertTrue(rel.mais_cedo(self.unit.Relogio(21, 15, 50)))

if __name__ == '__main__':
    unittest.main()
