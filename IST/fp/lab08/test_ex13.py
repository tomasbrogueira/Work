#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_repr(self):
        ''' Test sequence for 'repr()' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(repr(rel), "20:15:50")
    def test_hora(self):
        ''' Test sequence for '.horas()' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel._horas(), 20)
    def test_min(self):
        ''' Test sequence for '.minutos()' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel._minutos(), 15)
    def test_seg(self):
        ''' Test sequence for '.segundos()' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertEqual(rel._segundos(), 50)
    def test_relogio(self):
        ''' Test sequence for '.eh_relogio(rel)' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertTrue(self.unit.Relogio.eh_relogio(rel))
    def test_lista(self):
        ''' Test sequence for '.eh_relogio([20, 15, 50])' '''
        self.assertFalse(self.unit.Relogio.eh_relogio([20, 15, 50]))
    def test_string(self):
        ''' Test sequence for '.eh_relogio("20:15:50")' '''
        self.assertFalse(self.unit.Relogio.eh_relogio("20:15:50"))
    def test_int(self):
        ''' Test sequence for '.eh_relogio(20_15_50)' '''
        self.assertFalse(self.unit.Relogio.eh_relogio(20_15_50))
    def test_mesmas(self):
        ''' Test sequence for '.mesmas_horas()' '''
        rel = self.unit.Relogio(20, 15, 50)
        rel2 = self.unit.Relogio(20, 15, 50)
        self.assertTrue(rel.mesmas_horas(rel2))
        self.assertTrue(rel2.mesmas_horas(rel))
    def test_antes(self):
        ''' Test sequence for 'antes' '''
        rel = self.unit.Relogio(20, 15, 50)
        self.assertTrue(rel.antes(self.unit.Relogio(21, 15, 50)))
    def test_nao_antes(self):
        ''' Test sequence for 'não antes' '''
        rel = self.unit.Relogio(20, 15, 50)
        rel2 = self.unit.Relogio(21, 15, 50)
        self.assertFalse(rel2.antes(rel))
    def test_depois(self):
        ''' Test sequence for 'depois' '''
        rel = self.unit.Relogio(21, 15, 50)
        rel2 = self.unit.Relogio(20, 15, 50)
        self.assertTrue(rel2.antes(rel))
    def test_nao_depois(self):
        ''' Test sequence for 'não depois' '''
        rel = self.unit.Relogio(21, 15, 50)
        rel2 = self.unit.Relogio(20, 15, 50)
        self.assertFalse(rel.antes(rel2))
    def test_diferenca(self):
        ''' Test sequence for '.diferenca()' '''
        rel = self.unit.Relogio(20, 15, 50)
        rel2 = self.unit.Relogio(21, 15, 50)
        self.assertEqual(3600, rel2.diferenca(rel))

if __name__ == '__main__':
    unittest.main()
